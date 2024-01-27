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

# Create your views here.
# @login_required
# def List_Utilisateur_Cle(request,pk):
#     utilisateur =Utilisateur.objects.get(id=pk)      
#     context = {
#           'utilisateur':utilisateur,
#           'id':pk
#       }
#     return render(request, 'utilisateur/List_Utilisateur_Cle.html',context)

# @login_required
# def utilisateurCreate(request):
#    form = AjouterUtilisateurForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = AjouterUtilisateurForm()
#        return redirect('accueil')
#    return render(request, 'utilisateur/Ajouter_Utilisateur.html', {'form':form})


@login_required
def List_Membre(request): 
   liste_membre = Membre.objects.all()
   total_membre = Membre.objects.count()
   myFilter = MembreFiltre(request.GET, queryset=liste_membre)
   liste_membre=myFilter.qs
   context = {
      "membre" : liste_membre,
      'total_membre': total_membre,
      'myFilter':myFilter,
      }
   return render(request, 'membre/List_Membre.html',context)

# @login_required
# def Modifier_Utilisateur(request,pk):
#    utilisateur=Utilisateur.objects.get(id=pk)
#    form=UtilisateurForm(instance=utilisateur)

#    if request.method=='POST':
#       form=UtilisateurForm(request.POST, instance=utilisateur)
#       if form.is_valid():
#          form.save()
#          return redirect('accueil')
#    context={'form':form}
#    return render(request, 'utilisateur/Ajouter_Utilisateur.html', context)

# @login_required
# def Supprimer_Utilisateur(request,pk):
#    utilisateur=Utilisateur.objects.get(id=pk)
#    if request.method=='POST':
#       utilisateur.delete()
#       return redirect('accueil')
#    context={'item':utilisateur}
#    return render(request, 'utilisateur/Supprimer_Utilisateur.html', context)

