from django.db import models
from membre.models import Membre
from django.utils import timezone
#from modeltranslation.translator import TranslationOptions, register
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    membre=models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    objet=models.CharField(max_length=200, null=True)
    texte=models.TextField(max_length=200, null=True)
    date=models.DateTimeField(default=timezone.now, null=True)
    en_attente=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.objet} - {self.membre if self.membre else 'Aucun Membre'}"
 




    

