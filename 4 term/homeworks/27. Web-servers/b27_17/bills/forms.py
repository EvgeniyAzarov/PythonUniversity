from django import forms


class BillForm(forms.Form):
    number = forms.IntegerField(label="Number:")
    date = forms.DateField(label="Date:")
    client = forms.ChoiceField()

