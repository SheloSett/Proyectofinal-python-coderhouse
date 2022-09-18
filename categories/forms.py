from socket import fromshare
from django import forms

class Formulario_categories(forms.Form):

    name = forms.CharField(max_length=40)
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    image = forms.ImageField(required=False)