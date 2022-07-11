from django import forms
from myapp.models import Order


class InterestForm(forms.Form):
    CHOICES = [(1, 'Yes'),
               (0, 'No')]

    interested = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    levels = forms.IntegerField(min_value=1)
    comments = forms.CharField(
        widget=forms.Textarea, label="Additional Comments")


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Student', 'courses', 'level', 'order_date']
        widgets = {
            'student': forms.RadioSelect,
            'order_date': forms.SelectDateWidget
        }
