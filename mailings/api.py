from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView

from .models import Client
from .models import Mailing

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
