from django.contrib import admin
from .models import Etat

# Register your models here.
class EtatAdmin(admin.ModelAdmin):
    exclude = ['cumVers', 'ecart']  # Remplacez 'nom_de_votre_attribut' par le nom de l'attribut que vous souhaitez exclure

admin.site.register(Etat, EtatAdmin)