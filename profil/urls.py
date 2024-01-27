from django.urls import path
from . import views
#from .views import Edit_Profile
#from .views import change_password
#from .views import CustomPasswordChangeView
#from django.contrib.auth import views as auth_views
from .views import change_user_and_password


urlpatterns = [
    #path('mon_profil',Edit_Profile, name='mon_profil'), 
#     path('password/', CustomPasswordChangeView.as_view(), name='password'), 
#       path('password/', auth_views.PasswordChangeView.as_view()), 
#       path('password/done/', auth_views.PasswordChangeDoneView.as_view()), 
     #path('change_password/', change_password, name='change_password'),
     path('change_user_and_password.html/', change_user_and_password, name='change_user_and_password'),
 ]
