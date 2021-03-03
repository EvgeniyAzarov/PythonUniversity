from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Bill(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)

    def __str__(self):
        bill_info = [
            str(self.number),
            self.client.name
        ]
        return " ".join(bill_info)


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def __str__(self):
        item_info = [
            self.product.name,
            str(self.quantity),
            self.product.unit
        ]
        return " ".join(item_info)
