from django.db import models
from etat.models import Etat
from django.contrib.auth.models import User
from django.utils import timezone
#from modeltranslation.translator import TranslationOptions, register

# Create your models here.
class Versement(models.Model):
    membre=models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    montant=models.IntegerField(null=True)
    date=models.DateTimeField(default=timezone.now, null=True)

#@register(Versement)  
#class VersementTranslationOptions(TranslationOptions):
#    fields = ('membre', 'montant', 'date',) 