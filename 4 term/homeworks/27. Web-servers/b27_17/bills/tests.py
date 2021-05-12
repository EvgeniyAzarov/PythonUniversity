from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from django.db import IntegrityError

from .models import Client
from .models import Product
from .models import Bill
from .models import BillItem


class ModelsTests(TestCase):

    def setUp(self):
        self.client = Client.objects.create(name="Test Client", email="test@test.com")

    def test_unique_bill_number_error(self):
        Bill.objects.create(number=1, client=self.client, date=timezone.now())
        with self.assertRaises(IntegrityError):
            Bill.objects.create(number=1, client=self.client, date=timezone.now())

    def test_unique_bill_number_regular(self):
        Bill.objects.create(number=1, client=self.client, date=timezone.now())
        bill = Bill.objects.create(number=2, client=self.client, date=timezone.now())
        self.assertEqual(str(bill), "2 " + self.client.name)

    def test_delete_cascade(self):
        self.client.delete()
        bills = Bill.objects.filter(client__name=self.client.name)
        self.assertQuerysetEqual(bills, [])


class BillsIndexViewTests(TestCase):

    def setUp(self):
        self.clt = Client.objects.create(name="Test Client", email="test@test.com")

    def test_no_bills(self):
        response = self.client.get(reverse('bills:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No bills are available.")
        self.assertQuerysetEqual(response.context['bills_list'], [])

    def test_add_bill(self):
        Bill.objects.create(number=1, client=self.clt, date=timezone.now())
        response = self.client.get(reverse('bills:index'))
        self.assertQuerysetEqual(
            response.context['bills_list'],
            ['<Bill: 1 Test Client>']
        )
