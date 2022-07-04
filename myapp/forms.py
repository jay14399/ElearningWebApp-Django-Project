from django import forms
from myapp.models import Order


class InterestForm(forms.Form):
    CHOICES = [(1, 'Yes'),
               (0, 'No')]

    interested = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    levels = forms.IntegerField(default=1, min_value=1)
    comments = forms.CharField(widget=forms.Textarea, blank=True, label="Additional Comments")