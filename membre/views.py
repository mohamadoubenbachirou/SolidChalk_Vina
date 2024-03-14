from django.shortcuts import render,redirect,HttpResponse
from .models import Membre
from .forms import AjouterMembreForm
from django.contrib.auth.decorators import login_required
from etat.models import Etat
from post.models import Post
from versement.models import Versement
from django.contrib import messages
from .forms import MembreForm
from .filters import MembreFiltre
from django.db.models import Sum
from membre.models import PointFocal 
from .forms import CreerUtilisateur
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your views here.
# @login_required
# def List_Utilisateur_Cle(request,pk):
#     utilisateur =Utilisateur.objects.get(id=pk)      
#     context = {
#           'utilisateur':utilisateur,
#           'id':pk
#       }
#     return render(request, 'utilisateur/List_Utilisateur_Cle.html',context)

@login_required
def membreCreate(request):
   form = AjouterMembreForm(request.POST or None)
   if form.is_valid():
       form.save()
       form = AjouterMembreForm()
       return redirect('membre')
   return render(request, 'membre/Ajouter_Membre.html', {'form':form})


@login_required
def List_Membre(request): 
   liste_membre = Membre.objects.all()
   total_membre = Membre.objects.count()
   myFilter = MembreFiltre(request.GET, queryset=liste_membre)
   liste_membre=myFilter.qs
   # membres = Membre.objects.annotate(total_versement=Sum('versements__montant'))
   # for membre in membres:
   #   membre.actif = membre.est_actif

   context = {
      "membre" : liste_membre,
      'total_membre': total_membre,
      'myFilter':myFilter,
      }
   if request.user.is_authenticated:
        is_point_focal = request.user.groups.filter(name='Points focaux').exists()
        context['is_point_focal'] = is_point_focal
   return render(request, 'membre/List_Membre.html',context)

@login_required
def Modifier_Membre(request,pk):
   membre=Membre.objects.get(id=pk)
   form=MembreForm(instance=membre)

   if request.method=='POST':
      form=MembreForm(request.POST, instance=membre)
      if form.is_valid():
         form.save()
         return redirect('membre')
   context={'form':form}
   return render(request, 'membre/Ajouter_Membre.html', context)
   

@login_required
def Supprimer_Membre(request,pk):
   membre=Membre.objects.get(id=pk)
   if request.method=='POST':
      membre.delete()
      return redirect('membre')
   context={'item':membre}
   return render(request, 'membre/Supprimer_Membre.html', context)

@login_required
def creer_point_focal(request):
    return render(request, 'membre/creer_point_focal.html')




