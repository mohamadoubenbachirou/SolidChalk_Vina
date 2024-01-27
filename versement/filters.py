import django_filters
from .models import Versement

class VersementFiltre(django_filters.FilterSet):
    class Meta:
        model=Versement
        fields='__all__'
        exclude=['membre', 'date']
