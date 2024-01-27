from django.db import models
from membre.models import Membre
from django.utils import timezone
#from modeltranslation.translator import TranslationOptions, register

# Create your models here.
class Post(models.Model):
    membre=models.ForeignKey(Membre, null=True, on_delete=models.SET_NULL)

    objet=models.CharField(max_length=200, null=True)
    texte=models.TextField(max_length=200, null=True)
    date=models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.membre.nom
 

#@register(Post)  
#class PostTranslationOptions(TranslationOptions):
#    fields = ('membre', 'objet', 'texte', 'date',)  


    

