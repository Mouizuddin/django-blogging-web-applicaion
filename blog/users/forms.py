from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class MetaData:
        model = User
        fileds = ['username' , 'email' , 'password1' ,'password2']