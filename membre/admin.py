from django.contrib import admin
from .models import Membre

# Register your models here.
class MembreAdmin(admin.ModelAdmin):
    exclude = ['nom','ajour', 'actif']  # Remplacez 'nom_de_votre_attribut' par le nom de l'attribut que vous souhaitez exclure
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Si l'utilisateur est superutilisateur, afficher tous les membres
        # Filtrer les membres par établissement du point focal connecté
        return qs.filter(etablissement=request.user.membre.etablissement)

admin.site.register(Membre, MembreAdmin)