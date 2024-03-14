from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from django.utils.translation import gettext as _

# class CreerUtilisateur(UserCreationForm):
#     class meta:
#         model=User
#         fields=['username','password1','password2']

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django import forms 
# from membre.models import PointFocal, Etablissement

# class CreerUtilisateur(UserCreationForm):
#     class meta:
#         model=User
#         fields=['username','password1','password2']


class CreerUtilisateur(UserCreationForm):
    
    # Créez une liste de tuples (valeur, libellé) pour la liste déroulante
    CHOICES = [('DRES', 'DRES'),
    ('Lycée classique de Ngaoundére', 'Lycée classique de Ngaoundére'),
    ('Lycée Bilingue de Ngaoundére', 'Lycée Bilingue de Ngaoundére'), 
    ('Lycée de Ngaoundére Mardock', 'Lycée de Ngaoundére Mardock'),
    ('Collège Polyvalent Bilingue la Victoire', 'Collège Polyvalent Bilingue la Victoire'),
    ('Institut Polyvalent Bilingue le Pintades', 'Institut Polyvalent Bilingue le Pintades'),
    ('Lycée de Burkina', 'Lycée de Burkina')
    ]
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
    
    # Définissez le champ de formulaire comme un ChoiceField avec les choix que vous avez créés
    # etablissement = forms.ChoiceField(choices=CHOICES)
    # region = forms.ChoiceField(choices=REGION)
    # departement = forms.ChoiceField(choices=DEPARTEMENT)
    #discipline = forms.ChoiceField(choices=DISCIPLINE)
    #dateService=forms.DateTimeField()

    class Meta(UserCreationForm.Meta):
        model = User
        #fields = ['username', 'password1', 'password2', 'discipline', 'dateService']
        fields = ['username', 'password1', 'password2']
