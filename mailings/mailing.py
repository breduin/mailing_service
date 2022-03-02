from django_rq import job
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
    for client in clients:
        data = {
            "phone": client.phonenumber,
            "text": mailing.text
        }
        response = requests.post(MAILING_URL, data=data)
        Message.objects.create(
            sent_at=now(),
            status=response.status_code,
            mailing=mailing,
            client=client,
            )
long_running_func.delay()


@receiver(post_save, sender=Mailing)
def handle_mailing(sender, instance, **kwargs):
    print(kwargs)
    mailing = instance
    tags = [tag.strip() for tag in mailing.tags.split(',')]
    codes = [code.strip() for code in mailing.mobile_codes.split(',')]
    logger.DEBUG('тэги: %s, коды: %s', ','.join(tags), ','.join(codes))
    clients = Client.objects.filter(tag__in=tags).filter(mobile_code__in=codes)
    if mailing.start_at < now() and mailing.stop_at > now():
        start_mailing(mailing, clients)
