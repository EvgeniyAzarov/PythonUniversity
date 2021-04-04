import json
import xml.etree.ElementTree as et
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.conf import settings
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


def bill_view(request, bill_id):
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


def prepare_data():
    data = []
    bills = Bill.objects.all()

    for bill in bills:
        bill_dict = {
            'bill_id': bill.id,
            'number': bill.number,
            'client': {
                'id': bill.client.id,
                'name': bill.client.name,
                'email': bill.client.email,
            }
        }

        items = BillItem.objects.filter(bill=bill.id)
        items_list = []
        for item in items:
            item_dict = {
                'id': item.id,
                'product': {
                    'id': item.product.id,
                    'name': item.product.name,
                    'unit': item.product.unit,
                    'price': item.product.price,
                },
                'quantity': item.quantity,
            }
            items_list.append(item_dict)

        bill_dict['items'] = items_list
        data.append(bill_dict)

    return data


def data_to_xml(data):
    root = et.Element('bills')

    for bill in data:
        bill_el = et.SubElement(root, 'bill', {
            'bill_id': str(bill['bill_id']),
            'number': str(bill['number']),
        })
        et.SubElement(bill_el, 'client', {
            'id': str(bill['client']['id']),
            'name': bill['client']['name'],
            'email': bill['client']['email']
        })

        items_el = et.SubElement(bill_el, 'items')
        for item in bill['items']:
            item_el = et.SubElement(items_el, 'item', {
                'id': str(item['id']),
                'quantity': str(item['quantity'])
            })
            et.SubElement(item_el, 'product', {
                'id': str(item['product']['id']),
                'name': item['product']['name'],
                'unit': item['product']['unit'],
                'price': str(item['product']['price'])
            })

    return root


def export_data(request, action):
    data = prepare_data()

    if action == "previewXml":
        xmltree = data_to_xml(data)
        data_xml = et.tostring(xmltree, encoding='unicode', method='xml')
        return HttpResponse(data_xml, content_type="application/xml")
    elif action == "previewJson":
        data_json = json.dumps(data, indent=4)
        return HttpResponse(data_json, content_type="application/json")
    elif action == "downloadXml":
        filepath = str(settings.BASE_DIR) + '/storage/files/data_export.xml'
        with open(filepath, 'w') as file:
            xmltree = et.ElementTree(data_to_xml(data))
            xmltree.write(file, encoding='unicode', xml_declaration=True)

        file = open(filepath, 'r')
        mime_type = "application/xml"
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename={}" \
            .format('data_export.xml')
        return response
    elif action == "downloadJson":
        filepath = str(settings.BASE_DIR) + '/storage/files/data_export.json'
        print(filepath)
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)

        file = open(filepath, 'r')
        mime_type = "application/json"
        response = HttpResponse(file, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename={}"\
            .format('data_export.json')
        return response
    else:
        raise Http404("Not allowed action")
