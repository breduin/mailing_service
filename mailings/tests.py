"""
Test of mailings API
"""
from django.test import TestCase
from django.urls import reverse

from .models import Client
from .models import Mailing


class TestMailingsAPI(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(
            phonenumber='+79111234567',
            mobile_code=911,
            tag='one'

            )


    def test_create_client(self):
        data = {
            "phonenumber": "+79211234567",
            "mobile_code": 921,
            "tag": "one",
            "time_zone": "UTC+3"
            }
        response = self.client.post(
            reverse('add_client'),
            data=data,
            )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Client.objects.count(), 2)
