from django.shortcuts import render, redirect
from .forms import VersementForm
from .models import Versement
from membre.models import Membre
from django.contrib.auth.decorators import login_required
from .forms import FaireVersementForm
from django.contrib import messages

# Create your views here.
@login_required
def List_Versement(request):
   #liste_versement = Versement.objects.all()
   total_versement = Versement.objects.count()
   #user_instance = Utilisateur.objects.get(User=request.user.username)
   user_versement = Versement.objects.filter(membre=request.user)
   context = {
      #"versement" : liste_versement,
      'total_versement': total_versement,
      'user_versement': user_versement
      }
   return render(request, 'versement/List_Versement.html', context)

# @login_required
# def Ajouter_Versement(request):
#    form=VersementForm()
#    if request.method=='POST':
#       form=VersementForm(request.POST)
#       if form.is_valid():
#          form.save()
#          return redirect('accueil')
#    context={'form':form}
#    return render(request, 'versement/Ajouter_Versement.html', context)

# @login_required
# def Modifier_Versement(request,pk):
#    versement=Versement.objects.get(id=pk)
#    form=VersementForm(instance=versement)

#    if request.method=='POST':
#       form=VersementForm(request.POST, instance=versement)
#       if form.is_valid():
#          form.save()
#          return redirect('accueil')
#    context={'form':form}
#    return render(request, 'versement/Ajouter_Versement.html', context)

# @login_required
# def Supprimer_Versement(request,pk):
#    versement=Versement.objects.get(id=pk)
#    if request.method=='POST':
#       versement.delete()
#       return redirect('accueil')
#    context={'item':versement}
#    return render(request, 'versement/Supprimer_Versement.html', context)

# @login_required
# def Faire_Versement(request):
#    form = FaireVersementForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = FaireVersementForm()
#        return redirect('accueil')
#    return render(request, 'versement/Faire_Versement.html', {'form':form})

# @login_required
# def List_Versement_Cle(request, pk):
#     versement =Versement.objects.get(id=pk)   

#     context = {
#           'versement':versement,
#           'id':pk
#       }
#     return render(request, 'versement/List_Versement_Cle.html',context)
