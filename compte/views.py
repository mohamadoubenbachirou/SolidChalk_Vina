from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreerUtilisateur
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreerUtilisateur
from versement.forms import FaireVersementForm
from versement.models import Versement
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from membre.models import Membre

# Create your views here.
#@login_required(login_url='acces')
def inscriptionPage(request):
    form=CreerUtilisateur(request.POST or None)
    if request.method=="POST":
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            
            #discipline = form.cleaned_data['discipline']
            #date_service = form.cleaned_data['dateService']
            #membre = Membre.objects.create(user=request.user, discipline=discipline, dateService=date_service)
            membre=form.save()
            versement=Versement(membre=membre, montant=2100)
            versement.save()
            return redirect('membre')
    context={'form':form}
    return render(request, 'compte/inscription.html', context)



def accesPage(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Stocke le nom d'utilisateur dans le cookie de session sécurisé
            request.session['username'] = username
            request.session['password'] = password

            # Définir le cookie comme sécurisé
            request.session.modified = True
            request.session.save()

            return redirect('accueil')
        else:
            messages.info(request, "Il y a une erreur dans le nom d'utilisateur et/ou le mot de passe")

    return render(request, 'compte/acces.html', context)


#@login_required(login_url='acces')
def logoutUser(request):
    if request.user.is_authenticated:
       logout(request)
       if not request.user.is_authenticated:
        print(request.session.items())
    return redirect('acces')

