import django_filters
from .models import Membre

class MembreFiltre(django_filters.FilterSet):
    class Meta:
        model=Membre
        fields=['region', 'departement', 'etablissement', 'discipline']