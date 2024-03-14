from django.db import models
from etat.models import Etat 
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from membre.models import Membre

# Create your models here.
class Versement(models.Model):
    membre=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    montant=models.IntegerField(null=True)
    date=models.DateTimeField(default=timezone.now, null=True)
    #motif = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.montant} - {self.membre.username if self.membre else 'Aucun Utilisateur'}"

# @receiver(post_save, sender=Versement)
# def update_cumulative(sender, instance, **kwargs):
#     if instance.membre:
#         etat_obj, created = Etat.objects.get_or_create(user=instance.membre)
#         etat_obj.cumVers = (etat_obj.cumVers or 0) + instance.montant
#         etat_obj.save()

@receiver(post_save, sender=Versement)
def update_etat_cumulative(sender, instance, created, **kwargs):
    if created:  # Vérifie si l'instance de Versement est nouvellement créée
        montant_versement = instance.montant
        membre = instance.membre
        if membre:
            membre_instance = Membre.objects.get(user=membre)
            etat, created = Etat.objects.get_or_create(membre=membre_instance)
            etat.cumVers += montant_versement
            etat.save()
