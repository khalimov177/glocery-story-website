from django import forms
from .models import *

class OrderForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

    class Meta:
        model = Order
        fields = ['address', 'phone']

class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea'}))

    class Meta:
        model = Review
        fields = ['text']