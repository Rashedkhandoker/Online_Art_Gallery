from django import forms
from .models import Artwork


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ('title','status','medium','category','art_description','art')
