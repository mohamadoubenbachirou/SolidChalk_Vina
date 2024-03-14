from django.db import models
from membre.models import Membre
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Etat(models.Model):
    membre = models.OneToOneField(Membre, on_delete=models.CASCADE)
    cumAtt = models.IntegerField(null=True, default=0)
    cumVers = models.IntegerField(null=True, default=0)
    ecart = models.IntegerField(blank=True, null=True)
    sortie = models.IntegerField(null=True, default=0)
    motif = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        # Calcul de l'écart
        self.ecart = self.cumVers - self.cumAtt
        super(Etat, self).save(*args, **kwargs)
    
    def __str__(self):
        if self.membre:
            return f"{self.membre} - {self.cumAtt} - {self.cumVers} - {self.ecart}"
        else:
            return f"{self.cumAtt} - {self.cumVers} - {self.ecart}"

# @receiver(post_save, sender=Etat)
# def update_ecart(sender, instance, **kwargs):
#     # Mettre à jour l'écart chaque fois que cumAtt est modifié
#     if instance.cumAtt is not None and instance.cumVers is not None:
#         instance.ecart = instance.cumVers - instance.cumAtt
#         instance.save(update_fields=['ecart'])