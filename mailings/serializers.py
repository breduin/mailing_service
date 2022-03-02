from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField

from .models import Client
from .models import Mailing
from .models import Message


class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class MailingSerializer(ModelSerializer):

    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    mailing = PrimaryKeyRelatedField(
        allow_empty=False,
        queryset=Mailing.objects.all(),
        )
    client = PrimaryKeyRelatedField(
        allow_empty=False,
        queryset=Client.objects.all(),
        )

    class Meta:
        model = Message
        fields = [
            'id',
            'sent_at',
            'is_sent',
            'mailing',
            'client',
            ]
