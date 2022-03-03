from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView

from django.http import JsonResponse

from .mailing import handle_mailing
from .models import Client
from .models import Mailing
from .models import Message

from .serializers import ClientSerializer
from .serializers import MailingSerializer


class ClientCreateView(CreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientGetView(RetrieveAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientDeleteView(DestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientUpdateView(UpdateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientsListView(ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    model = Client


class MailingCreateView(CreateAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()


class MailingGetView(RetrieveAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()


class MailingDeleteView(DestroyAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()


class MailingUpdateView(UpdateAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()


class MailingsListView(ListAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()
    model = Mailing


@api_view(['GET'])
def push_active_mailings(request):
    active_mailings = Mailing.objects.filter(is_active=True)
    for mailing in active_mailings:
        handle_mailing(mailing)
    response = {
        'mailings': active_mailings.count(),
    }
    return JsonResponse(response)


@api_view(['GET'])
def get_statistics(request):
    mailings = Mailing.objects.all()
    messages = Message.objects.all()
    response = {
        'active_mailings': mailings.filter(is_active=True).count(),
        'sent_mailings': mailings.filter(is_active=False).count(),
        'messages_total': messages.count(),
        'success_messages': messages.filter(
            status__in=range(200, 300)
            ).count(),
    }
    return JsonResponse(response)
