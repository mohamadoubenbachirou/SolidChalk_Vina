from django.urls import path
from . import views

urlpatterns = [
    path('',views.List_Versement, name='versement'), 
    # path('ajout_versement',views.Ajouter_Versement, name='ajout_versement'), 
    # path('modifier_versement/<str:pk>',views.Modifier_Versement, name='modifier_versement'), 
    # path('supprimer_versement/<str:pk>',views.Supprimer_Versement, name='supprimer_versement'), 
    # path('faire_versement', views.Faire_Versement, name='faire_versement'), 
    # path('<str:pk>', views.List_Versement_Cle, name='versement_cle'),  
]