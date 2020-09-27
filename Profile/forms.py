from django import forms
from .models import Profile
from django.forms import ModelForm

class Profileform(ModelForm):
    class Meta:
        model = Profile
<<<<<<< Updated upstream
        fields =('Full_name','email','contact_no','Profile_picture')
=======
        fields = '__all__'
>>>>>>> Stashed changes
