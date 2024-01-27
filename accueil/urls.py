from django.urls import path
from . import views
from compte.views import accesPage
#from .views import ChangeLanguageView
from .views import change_language

urlpatterns = [
    path('home',views.home, name='accueil'), 
    path('',accesPage, name='connexion'), 
    path('recherche', views.recherche, name='recherche'),
    path('',views.List_Etat, name='etat'), 
    path('',views.List_Post, name='post'), 
    path('liste_membre', views.List_Membre, name='membre'),
    path('',views.List_Versement, name='versement'), 
    #path("openfile/<str:pk>",views.ouvrir_pdf,name = "pdfread")
    path('change_language/', change_language, name='change_language'),
    

]