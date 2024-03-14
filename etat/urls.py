from django.urls import path
from . import views

urlpatterns = [
    path('',views.List_Etat, name='etat'), 
    path('ajout_etat',views.Ajouter_Etat, name='ajout_etat'), 
    path('modifier_etat/<str:pk>',views.Modifier_Etat, name='modifier_etat'), 
    path('supprimer_etat/<str:pk>',views.Supprimer_Etat, name='supprimer_etat'), 
    path('definir_etat', views.Definir_Etat, name='definir_etat'), 
    #path('<str:pk>', views.List_Etat_Cle, name='etat_cle'),  
] 