from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Bill, BillItem, Client
from .forms import BillForm


def index(request):
    bills_list = Bill.objects.all()
    context = {"bills_list": bills_list}
    return render(request, 'bills/index.html', context)


def add(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            bill_data = form.cleaned_data
            new_bill = Bill(number=bill_data['number'],
                            date=bill_data['date'],
                            client=Client.objects.get(id=bill_data['client']))
            new_bill.save()
        return HttpResponseRedirect('/')
    else:
        form = BillForm()
        return render(request, "bills/add.html", {'form': form})


def bill(request, bill_id):
    context = {}
    bill_name = str(Bill.objects.get(id=bill_id))
    context['bill'] = bill_name
    items = BillItem.objects.filter(bill_id=bill_id)
    context['bill_items'] = items
    return render(request, "bills/bill.html", context)
