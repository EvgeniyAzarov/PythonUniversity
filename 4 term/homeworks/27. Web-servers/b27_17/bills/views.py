from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Bill, BillItem, Client, Product
from .forms import BillForm, ItemForm


def index(request):
    bills_list = Bill.objects.all()
    context = {"bills_list": bills_list}
    return render(request, 'bills/index.html', context)


def add(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_bill = Bill(number=data['number'],
                            date=data['date'],
                            client=Client.objects.get(id=data['client']))
            new_bill.save()
        return HttpResponseRedirect('/')
    else:
        form = BillForm()
        return render(request, "bills/add.html", {'form': form})


def delete(request, bill_id):
    bill_obj = Bill.objects.get(id=bill_id)
    bill_obj.delete()
    return HttpResponseRedirect('/')


def bill(request, bill_id):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            bill_item = BillItem(bill_id=bill_id,
                                 product=Product.objects.get(id=data['product']),
                                 quantity=data['quantity'])
            bill_item.save()
        return HttpResponseRedirect(request.path_info)
    else:
        context = {}

        form = ItemForm()
        context['form'] = form

        bill_obj = Bill.objects.get(id=bill_id)
        context['bill'] = bill_obj

        items = BillItem.objects.filter(bill_id=bill_id)
        bill_items = []
        for item in items:
            bill_items.append({
                'product': item.product.name,
                'quantity': str(item.quantity) + item.product.unit,
                'cost': item.product.price * item.quantity
            })
        context['bill_items'] = bill_items

        return render(request, "bills/bill.html", context)
