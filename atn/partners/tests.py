from django.test import TestCase
from .models import Client


class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name="firstClient", address="first street")
        Client.objects.create(name="secondClient", address="second street")

    def test_create_clients(self):
        """I can create clients"""
        first = Client.objects.get(name="firstClient")
        second = Client.objects.get(name="secondClient")
        assert first
        assert second

    def test_exception_when_none(self):
        with self.assertRaises(Client.DoesNotExist) as context:
          third = Client.objects.get(name="xxx")

          


