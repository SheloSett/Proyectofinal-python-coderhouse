from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class User_registration_form(UserCreationForm):
    username = forms.CharField(label="Usuario", max_length=30)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # widget muestra los asteriscos
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {k:"" for k in fields} # Saca los comentarios de ayuda

class User_profile_form(forms.Form):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(label='Apellido', max_length=30, required=False)
    phone = forms.CharField(max_length=20, required=False) 
    address = forms.CharField(max_length=200, required=False)
    image = forms.ImageField(required=False)
    



