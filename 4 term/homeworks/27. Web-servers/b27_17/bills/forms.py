from django import forms
from .models import Client, Product


class BillForm(forms.Form):
    number = forms.IntegerField(label="Number:")
    date = forms.DateField(label="Date:", widget=forms.DateInput(attrs={'type':'date'}))
    client = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        self.fields['client'] = forms.ChoiceField(
            choices=[(c.id, str(c)) for c in Client.objects.all()]
        )


class ItemForm(forms.Form):
    product = forms.ChoiceField()
    quantity = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['product'] = forms.ChoiceField(
            choices=[(p.id, str(p)) for p in Product.objects.all()]
        )
