from django.shortcuts import render, redirect
from .forms import EtatForm
from .models import Etat
from versement.models import Versement
from post.models import Post
from django.contrib.auth.decorators import login_required
from .forms import EtatVersementForm
from django.contrib import messages
from .filters import EtatFiltre

# Create your views here.
@login_required
def List_Etat(request):
   liste_etat = Etat.objects.all()
   total_etat = Etat.objects.count()
   myFilter = EtatFiltre(request.GET, queryset=liste_etat)
   liste_etat=myFilter.qs
   context = {
      "etat" : liste_etat,
      'total_etat': total_etat,
      'myFilter':myFilter,
      }
   return render(request, 'etat/List_Etat.html', context)

# @login_required
# def Ajouter_Etat(request):
#    form=EtatForm()
#    if request.method=='POST':
#       form=EtatForm(request.POST)
#       if form.is_valid():
#          form.save()
#          return redirect('accueil')
#    context={'form':form}
#    return render(request, 'etat/Ajouter_Etat.html', context)

# @login_required
# def Modifier_Etat(request,pk):
#    etat=Etat.objects.get(id=pk)
#    form=EtatForm(instance=etat)

#    if request.method=='POST':
#       form=EtatForm(request.POST, instance=etat)
#       if form.is_valid():
#          form.save()
#          return redirect('accueil')
#    context={'form':form}
#    return render(request, 'etat/Ajouter_Etat.html', context)

# @login_required
# def Supprimer_Etat(request,pk):
#    etat=Etat.objects.get(id=pk)
#    if request.method=='POST':
#       etat.delete()
#       return redirect('accueil')
#    context={'item':etat}
#    return render(request, 'etat/Supprimer_Etat.html', context)

# @login_required
# def Definir_Etat(request):
#    form = EtatVersementForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = EtatVersementForm()
#        return redirect('accueil')
#    return render(request, 'etat/Definir_Etat.html', {'form':form})


# @login_required
# def List_Etat_Cle(request, pk):
#     etat =Etat.objects.get(id=pk)   

#     context = {
#           'etat':etat,
#           'id':pk
#       }
#     return render(request, 'etat/List_Etat_Cle.html',context)
