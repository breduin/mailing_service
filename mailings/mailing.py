from django_rq import job
import logging
import requests

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from .models import Client
from .models import Message
from .models import Mailing


logger = logging.getLogger(__name__)


MAILING_URL = 'https://probe.fbrq.cloud/v1/send/1'


@job
def start_mailing(mailing, clients):
    logger.info(f'Mailing №{mailing.id}')
    for client in clients:
        data = {
            "phone": str(client.phonenumber),
            "text": mailing.text
        }
        response = requests.post(MAILING_URL, data=data)
        Message.objects.create(
            sent_at=now(),
            status=response.status_code,
            mailing=mailing,
            client=client,
            )
        Mailing.objects.filter(pk=mailing.pk).update(is_active=False)


start_mailing.delay()


def handle_mailing(mailing):
    clients = Client.objects.all()
    if mailing.tags:
        tags = [tag.strip() for tag in mailing.tags.split(',')]
        clients = clients.filter(tag__in=tags)
    if mailing.mobile_codes:
        codes = [int(code.strip()) for code in mailing.mobile_codes.split(',')]
        clients = clients.filter(mobile_code__in=codes)

    if all([
            mailing.start_at < now(),
            mailing.stop_at > now(),
            mailing.is_active
            ]):
        start_mailing(mailing, clients)


@receiver(post_save, sender=Mailing)
def handle_signal(sender, instance, created, **kwargs):
    if created:
        handle_mailing(instance)
