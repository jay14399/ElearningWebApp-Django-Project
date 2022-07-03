from socket import fromshare
from django import forms
from myapp.models import Order


class InterestForm(forms.Form):
    interested = forms.RadioSelect()
    levels = forms.IntegerField(min_value=1, initial=1)
    comments = forms.Textarea()

