from django.forms import ModelForm
from autocomp.models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'address_street', 'address_house', 'address_flat', 'address_postal_code', 'address_comment', 'phone']

"""
class CustomerForm(forms.Form):
    email = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    address_street = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street'}))
    address_house = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'House'}))
    address_flat = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Flat'}))
    address_postal_code = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}))
    address_comment = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment'}))
    phone = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))

"""
