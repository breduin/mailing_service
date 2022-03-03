'''
Test of mailings API
'''
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from .models import Client
from .models import Mailing


class TestMailingsAPI(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(
            phonenumber='+79111234567',
            mobile_code=911,
            tag='one',
            time_zone='UTC+3',
            )
        Client.objects.create(
            phonenumber='+79211234567',
            mobile_code=921,
            tag='one',
            time_zone='UTC+3',
            )
        Client.objects.create(
            phonenumber='+79311234567',
            mobile_code=931,
            tag='two',
            time_zone='UTC+3',
            )     


    def test_create_client(self):
        clients_number = Client.objects.count()
        data = {
            'phonenumber': '+79411234567',
            'mobile_code': 921,
            'tag': 'one',
            'time_zone': 'UTC+3'
            }
        response = self.client.post(
            reverse('add_client'),
            data=data,
            )

        self.assertTrue(response.status_code < 300)
        self.assertEqual(Client.objects.count(), clients_number + 1)
        self.assertEqual(
            Client.objects.get(phonenumber=data['phonenumber']).mobile_code, data['mobile_code']
            )

    def test_create_mailing(self):
        mailings_number = Mailing.objects.count()
        data ={
            'start_at': now(),
            'stop_at': now(),
            'text': 'Сообщение 1',
            'mobile_codes': '911, 921',
            'tags': 'one, two',
            }
        response = self.client.post(
            reverse('add_mailing'),
            data=data,
            )

        self.assertTrue(response.status_code < 300)
        self.assertEqual(Mailing.objects.count(), mailings_number + 1)    