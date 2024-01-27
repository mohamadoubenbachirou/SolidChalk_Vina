from django.forms import ModelForm
from .models import Versement
from django import forms

class VersementForm(ModelForm):
    class Meta:
        model= Versement
        fields=[ 'montant' ,'date' ]

class FaireVersementForm(forms.ModelForm):
    class Meta:
         model = Versement
         fields=['membre', 'montant' ,'date']



