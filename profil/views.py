from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import CustomUserChangeForm, CustomPasswordChangeForm


# Create your views here.
@login_required
def change_user_and_password(request):
   if request.method == 'POST':
      user_form = CustomUserChangeForm(request.POST, instance=request.user)
      password_form = CustomPasswordChangeForm(request.user, request.POST)
      if user_form.is_valid() and password_form.is_valid():
         user_form.save()
         user = password_form.save()
         update_session_auth_hash(request, user)
         messages.success(request, 'Modfications enregistres avec succes.')
         return redirect('accueil')
      else:
         messages.error(request, 'Veuiller corriger les erreurs ci-dessous.')
   else:
      user_form = CustomUserChangeForm(instance=request.user)
      password_form = CustomPasswordChangeForm(request.user)
   return render(request, 'profil/change_user_and_password.html', {'user_form':user_form, 'password_form':password_form})

