from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.
# class Manages_files(models.Model):
#     title=models.CharField(max_length=255)
#     file=models.FileField(upload_to="static/pdf")

#     def __str__(self):
#         return self.title

# class MonModele(models.Model):
#     fichier_pdf = models.FileField(upload_to="static/pdf")


class UserLanguage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(_('Language'), max_length=5, choices=settings.LANGUAGES)


