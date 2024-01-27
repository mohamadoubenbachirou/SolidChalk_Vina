import django_filters
from .models import Etat

class EtatFiltre(django_filters.FilterSet):
    class Meta:
        model=Etat
        fields=['cumAtt']