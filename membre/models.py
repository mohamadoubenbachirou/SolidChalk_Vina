from django.db import models
#from modeltranslation.translator import TranslationOptions, register
#import datetime

# Create your models here.
class Membre(models.Model):
    REGION=(('Adamaoua','Adamaoua'),('Centre','Centre'),('Est','Est'),('Extreme-Nord', 'Extreme-Nord'),('Littoral','Littoral'),('Nord', 'Nord'),('Nord-Ouest', 'Nord-Ouest'),('Ouest', 'Ouest'),('Sud', 'Sud'),('Sud-Ouest', 'Sud-Ouest'))
    DEPARTEMENT=(('Vina','Vina'),('Djerem','Djerem'))
    ETABLISSEMENT=(('DRES','DRES'),('Lycée classique','Lycée classique'),('Lycée bilingue','Lycée bilingue'))
    DISCIPLINE=(('Mathematiques','Mathematiques'),('Informatique','Informatique'),('Physique','Physique'))
    ACTIF=(('Actif','Actif'),('Pas Actif','Pas Actif'))
    AJOUR=(('Ajour','Ajour'),('Pas Ajour','Pas Ajour'))
    nom=models.CharField(max_length=200, null=True)
    matricule=models.CharField(max_length=200, null=True)
    region=models.CharField(max_length=200, null=True, choices=REGION)
    departement=models.CharField(max_length=200, null=True, choices=DEPARTEMENT)
    etablissement=models.CharField(max_length=200, null=True, choices=ETABLISSEMENT)
    discipline=models.CharField(max_length=200, null=True, choices=DISCIPLINE)
    telephone=models.IntegerField(null=True)
    #profile_picture=models.ImageField(upload_to='static/images', blank=True, null=True)
    ajour=models.CharField(max_length=200, null=True, choices=AJOUR )
    actif=models.CharField(max_length=200, null=True, choices=ACTIF)

    def __str__(self):
        return self.nom

#@register(Membre)  
#class MembreTranslationOptions(TranslationOptions):
#    fields = ('nom', 'matricule', 'region', 'departement', 'etablissement', 'discipline', 'telephone', 'ajour', 'actif',) 
    # class Visitor_Infos(models.Model):
    #     ip_adress = models.GenericIPAddressField()
    #     page_visited=models.TextField()
    #     event_date = models.DateTimeField(default=datetime)