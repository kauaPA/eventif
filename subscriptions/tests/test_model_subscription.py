from django.test import TestCase
from datetime import datetime
from subscriptions.models import Subscription

class SubscriptionModelTEst(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = "Kaua Almeida",
            cpf = "3123131241",
            email = "kauaalmeida@gmail.com",
            phone = "5392313123131",

        )
        self.obj.save()

    def test_create(self):
       

        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)