from django.forms import ModelForm
from django import forms
from .models import Membre
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import PointFocal, Etablissement

# class CreerUtilisateur(UserCreationForm):
#     class meta:
#         model=User
#         fields=['username','password1','password2']


class CreerUtilisateur(UserCreationForm):
    # Obtenez la liste des établissements
    #etablissements = Etablissement.objects.all()
    
    # Créez une liste de tuples (valeur, libellé) pour la liste déroulante
    CHOICES = [('DRES', 'DRES'),
    ('Lycée classique de Ngaoundére', 'Lycée classique de Ngaoundére'),
    ('Lycée Bilingue de Ngaoundére', 'Lycée Bilingue de Ngaoundére'), 
    ('Lycée de Ngaoundére Mardock', 'Lycée de Ngaoundére Mardock'),
    ('Collège Polyvalent Bilingue la Victoire', 'Collège Polyvalent Bilingue la Victoire'),
    ('Institut Polyvalent Bilingue le Pintades', 'Institut Polyvalent Bilingue le Pintades'),
    ('Lycée de Burkina', 'Lycée de Burkina')
    ]
    
    # Définissez le champ de formulaire comme un ChoiceField avec les choix que vous avez créés
    etablissement = forms.ChoiceField(choices=CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2', 'etablissement']


# class MembreForm(ModelForm):
#     class Meta:
#          model=Membre
#          fields= "__all__"

class AjouterMembreForm(forms.ModelForm):
    class Meta:
         model = Membre
         fields = ['user','matricule', 'region','departement','etablissement', 'discipline', 'telephone', 'dateService']


class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['user','matricule', 'region','departement','etablissement', 'discipline', 'telephone','dateService']  # Les champs que vous voulez inclure dans le formulaire
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limitez le queryset pour le champ user à l'utilisateur actuel s'il est déjà un membre
        if self.instance.pk:  # Vérifie si l'instance existe déjà dans la base de données
            self.fields['user'].queryset = User.objects.filter(id=self.instance.user.id)
        else:
            self.fields['user'].queryset = User.objects.none()  # S'il s'agit d'une création, aucun utilisateur n'est sélectionné par défaut


# class PointFocalForm(forms.ModelForm):
#     class Meta:
#         model = Membre
#         fields = ['est_point_focal']