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
# @login_required
# def Edit_Profile(request):
#    if request.method == 'POST':
#       form = CustomUserChangeForm(request.POST, instance=request.user)
#       if form.is_valid():
#          form.save()
#          return redirect('accueil')
#    else:
#       form = CustomUserChangeForm(instance=request.user)
#    context={'form':form}
#    return render(request, 'profil/Mon_Profil.html', context)

# def change_password(request):
#    if request.method == 'POST':
#       form = PasswordChangeForm(request.user, request.POST)
#       if form.is_valid():
#          user = form.save()
#          update_session_auth_hash(request, user)
#          messages.success(request, 'Votre mot de passe a été modifié avec succes')
#          return redirect('accueil')
#       else:
#          messages.error(request, 'Veuiller corriger les erreurs ci-dessous.')
#    else:
#       form = PasswordChangeForm(request.user)
#    return render(request, 'profil/change_password.html', {'form':form})

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


# class CustomPasswordChangeView(PasswordChangeView):
#    template_name = 'profil/Mon_Profil.html'
#    success_url = reverse_lazy('accueil')

# class UserEditView(generic.UpdateView):
#    form_class = UserChangeForm
#    template_name = 'profil/Mon_Profil.html'
#    success_url = reverse_lazy('accueil')

#    def get_object(self):
#       return self.request.user