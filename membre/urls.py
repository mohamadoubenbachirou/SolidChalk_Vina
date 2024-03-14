from django.urls import path
from membre.views import membreCreate
from membre.views import List_Membre
from . import views



urlpatterns = [
    path('liste_membre', List_Membre, name='membre'),
    path('ajouter_membre', membreCreate, name='ajouter_membre'),
    path('modifier_membre/<str:pk>',views.Modifier_Membre, name='modifier_membre'), 
    path('supprimer_membre/<str:pk>',views.Supprimer_Membre, name='supprimer_membre'), 
    # path('<str:pk>', views.List_Utilisateur_Cle, name='utilisateur_cle'), 
    path('creer_point_focal/', views.creer_point_focal, name='creer_point_focal'),
    #path('inscription-point-focal/', views.inscription_point_focal, name='inscription_point_focal'),
     
]