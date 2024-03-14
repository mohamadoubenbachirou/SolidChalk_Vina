from django.contrib import admin
from .models import Versement

# Register your models here

@admin.register(Versement)
class VersementAdmin(admin.ModelAdmin):
    list_display = ('membre', 'montant')
