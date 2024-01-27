from django.db import models
from membre.models import Membre
#from modeltranslation.translator import TranslationOptions, register

# Create your models here.
class Etat(models.Model):
    membre=models.ForeignKey(Membre, null=True, on_delete=models.SET_NULL)

    cumAtt=models.IntegerField(null=True)
    cumVers=models.IntegerField(null=True)
    ecart=models.IntegerField(null=True)

    def __str__(self):
        return self.membre.nom

#@register(Etat)  
#class EtatTranslationOptions(TranslationOptions):
#    fields = ('membre', 'cumAtt', 'cumVers', 'ecart',)  

    