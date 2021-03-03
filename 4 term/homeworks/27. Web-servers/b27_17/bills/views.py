from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Bill, BillItem
from .forms import BillForm


def index(request):
    bills_list = Bill.objects.all()
    context = {"bills_list": bills_list}
    return render(request, 'bills/index.html', context)


def add(request):
    if request.methos == "POST":
        form = BillForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('/')
    else:
        form = BillForm()
        return render(request, "bills/add.html", {'form': form})
