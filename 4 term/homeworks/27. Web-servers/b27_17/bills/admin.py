from django.contrib import admin
from .models import BillItem, Bill, Client, Product

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(BillItem)

