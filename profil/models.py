from django.db import models
from django.contrib.auth.models import User
#from modeltranslation.translator import TranslationOptions, register

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(null=True, blank=True)
    profil_picture = models.ImageField(upload_to = 'images/', blank=True, null=True)

    def __str__(self):
        return self.user.username

