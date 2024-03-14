from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Etat

# @receiver(post_save, sender=Etat)
# def update_ecart(sender, instance, created, **kwargs):
#     if instance.cumVers is not None and instance.cumAtt is not None:
#         instance.ecart = instance.cumVers - instance.cumAtt
#         instance.save(update_fields=['ecart'])