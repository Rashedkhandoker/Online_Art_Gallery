from django import forms
from .models import User
from django.forms import ModelForm

class Userform(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'contact_no')
