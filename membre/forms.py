from django.forms import ModelForm
from django import forms
from .models import Membre

class MembreForm(ModelForm):
    class Meta:
         model=Membre
         fields= "__all__"

class AjouterMembreForm(forms.ModelForm):
    class Meta:
         model = Membre
         fields = ['nom','matricule', 'region','departement','etablissement', 'discipline', 'telephone', 'ajour', 'actif']

