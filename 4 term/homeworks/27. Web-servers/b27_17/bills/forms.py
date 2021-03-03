from django import forms
from .models import Client


class BillForm(forms.Form):
    number = forms.IntegerField(label="Number:")
    date = forms.DateField(label="Date:")
    client = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        self.fields['client'] = forms.ChoiceField(
            choices=[(c.id, str(c)) for c in Client.objects.all()]
        )
