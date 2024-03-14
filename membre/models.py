from django.db import models
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
#from membre.models import Etablissement



# Create your models here.

class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    REGION=(('Adamaoua',_('Adamaoua')),('Centre',_('Centre')),('Est',_('Est')),('Extreme-Nord', _('Extreme-Nord')),('Littoral',_('Littoral')),('Nord', _('Nord')),('Nord-Ouest', _('Nord-Ouest')),('Ouest', _('Ouest')),('Sud', _('Sud')),('Sud-Ouest', _('Sud-Ouest')))
    DEPARTEMENT=(('Vina','Vina'),('Djérem','Djérem'), ('Faro-et-Déo', 'Faro-et-Déo'), ('Mayo-Banyo', 'Mayo-Banyo'), ('Mbéré', 'Mbéré'))
    ETABLISSEMENT = (
    ('DRES', 'DRES'),
    ('Lycée classique de Ngaoundére', 'Lycée classique de Ngaoundére'),
    ('Lycée Bilingue de Ngaoundére', 'Lycée Bilingue de Ngaoundére'), 
    ('Lycée de Ngaoundére Mardock', 'Lycée de Ngaoundére Mardock'),
    ('Collège Polyvalent Bilingue la Victoire', 'Collège Polyvalent Bilingue la Victoire'),
    ('Institut Polyvalent Bilingue le Pintades', 'Institut Polyvalent Bilingue le Pintades'),
    ('Lycée de Burkina', 'Lycée de Burkina')
)
    DISCIPLINE=(('Mathématiques','Mathématiques'),('Informatique','Informatique'),('PCT','PCT'), ('Francais', 'Francais'), ('HGE', 'HGE'), ('Anglais', 'Anglais'))
    nom=models.CharField(max_length=200, null=True)
    matricule=models.CharField(max_length=200, null=True)
    region=models.CharField(max_length=200, null=True, choices=REGION)
    departement=models.CharField(max_length=200, null=True, choices=DEPARTEMENT)
    etablissement=models.CharField(max_length=200, null=True, choices=ETABLISSEMENT)
    #etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, default=None, choices=ETABLISSEMENT)
    discipline=models.CharField(max_length=200, null=True, choices=DISCIPLINE)
    telephone=models.IntegerField(null=True)
    #profile_picture=models.ImageField(upload_to='static/images', blank=True, null=True)
    dateService = models.DateField(null=True)
    dateInscription=models.DateTimeField(default=timezone.now, null=True)
    ajour=models.CharField(max_length=200, null=True)
    actif=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.user.username

    @property
    def est_actif(self):
        return self.versements.filter(montant__gt=0).exists()
    
    @property
    def membres_ajoutes_par_point_focal(self):
        if self.user.groups.filter(name='Points focaux').exists():
            return Membre.objects.filter(point_focal=self)
        else:
            return None

# Définir la fonction qui sera appelée lorsque l'utilisateur est créé
@receiver(post_save, sender=User)
def create_member(sender, instance, created, **kwargs):
    if created:
        # Créer un membre associé à cet utilisateur
        Membre.objects.create(user=instance)

from etat.models import Etat
@receiver(post_save, sender=Membre)
def create_etat_for_new_membre(sender, instance, created, **kwargs):
    if created:
        Etat.objects.create(membre=instance)


class PointFocal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Autres champs spécifiques au point focal

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=Membre)
# def update_payment_status(sender, instance, created, **kwargs):
#     if created or instance.dateService != instance.dateInscription:
#         duration = instance.dateService - instance.dateInscription
#         # Vérifie si la durée dépasse 5 mois
#         if duration > timedelta(days=5 * 30):
#             # Déconnecter le signal temporairement
#             post_save.disconnect(update_payment_status, sender=Membre)
#             instance.actif = "Payer tous les cummules attendus"
#             instance.save()
#             # Reconnecter le signal
#             post_save.connect(update_payment_status, sender=Membre)


    