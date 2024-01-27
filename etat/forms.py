from django.forms import ModelForm
from .models import Etat
from django import forms

class EtatForm(ModelForm):
    class Meta:
        model=Etat
        fields=['cumAtt' ,'cumVers', 'ecart']

class EtatVersementForm(forms.ModelForm):
    class Meta:
         model = Etat
         fields=['membre', 'cumAtt' ,'cumVers', 'ecart']