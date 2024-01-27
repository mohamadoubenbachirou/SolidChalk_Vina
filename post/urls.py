from django.urls import path
from . import views

urlpatterns = [
    path('',views.List_Post, name='post'), 
    # path('ajout_post',views.Ajouter_Post, name='ajout_post'), 
    # path('modifier_post/<str:pk>',views.Modifier_Post, name='modifier_post'), 
    # path('supprimer_post/<str:pk>',views.Supprimer_Post, name='supprimer_post'), 
    # path('poster', views.Poster, name='poster'), 
    # path('<str:pk>', views.List_Post_Cle, name='post_cle'),
] 