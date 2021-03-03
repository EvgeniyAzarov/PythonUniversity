from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=20)
    price = models.FloatField()


class Bill(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
