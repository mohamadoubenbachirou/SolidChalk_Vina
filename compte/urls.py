from django.urls import path
from . import views

urlpatterns = [
    path('acces', views.accesPage, name='acces'), 
    path('quitter', views.logoutUser, name='quitter'), 
    path('inscription', views.inscriptionPage, name='inscription'), 
    
]  