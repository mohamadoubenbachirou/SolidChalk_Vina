from django.urls import path
#from utilisateur.views import utilisateurCreate
from membre.views import List_Membre
from . import views


urlpatterns = [
    path('liste_membre', List_Membre, name='membre'),
    # path('ajouter_utilisateur', utilisateurCreate, name='ajouter_utilisateur'),
    # path('modifier_utilisateur/<str:pk>',views.Modifier_Utilisateur, name='modifier_utilisateur'), 
    # path('supprimer_utilisateur/<str:pk>',views.Supprimer_Utilisateur, name='supprimer_utilisateur'), 
    # path('<str:pk>', views.List_Utilisateur_Cle, name='utilisateur_cle'), 
     
]