from django.shortcuts import render, redirect
from .forms import VersementForm
from .models import Versement
from membre.models import Membre
from django.contrib.auth.decorators import login_required
from .forms import FaireVersementForm
from django.contrib import messages
from etat.models import Etat
from django.db.models import F
from django.http import JsonResponse
from django.db.models import Sum

# Create your views here.
@login_required
def List_Versement(request):
   total_versement = Versement.objects.count()
   user_versement = Versement.objects.filter(membre=request.user)
   montant_total_versé = Versement.objects.filter(membre=request.user).aggregate(total_versé=Sum('montant'))['total_versé'] or 0
   # Récupérer l'objet Etat pour l'utilisateur connecté
   etat = Etat.objects.get(membre__user=request.user)
   # Calculer la somme des versements
   somme_versements = Versement.objects.aggregate(Sum('montant'))['montant__sum'] or 0

   context = {
      'total_versement': total_versement,
      'user_versement': user_versement,
      'montant_total_versé':montant_total_versé,
      'cumAtt': etat.cumAtt,
      'somme_versements': somme_versements
      }
   if request.user.is_authenticated:
        is_point_focal = request.user.groups.filter(name='Points focaux').exists()
        context['is_point_focal'] = is_point_focal
   return render(request, 'versement/List_Versement.html', context)

@login_required
def Ajouter_Versement(request):
   form=VersementForm()
   if request.method=='POST':
      form=VersementForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('versement')
   context={'form':form}
   return render(request, 'versement/Ajouter_Versement.html', context)

@login_required
def Modifier_Versement(request,pk):
   versement=Versement.objects.get(id=pk)
   form=VersementForm(instance=versement)

   if request.method=='POST':
      form=VersementForm(request.POST, instance=versement)
      if form.is_valid():
         form.save()
         return redirect('versement')
   context={'form':form}
   return render(request, 'versement/Ajouter_Versement.html', context)

@login_required
def Supprimer_Versement(request,pk):
   versement=Versement.objects.get(id=pk)
   if request.method=='POST':
      versement.delete()
      return redirect('versement')
   context={'item':versement}
   return render(request, 'versement/Supprimer_Versement.html', context)

@login_required
def Faire_Versement(request):
   form = FaireVersementForm(request.POST or None)
   if form.is_valid():
       form.save()
       form = FaireVersementForm()
       return redirect('versement')
   return render(request, 'versement/Faire_Versement.html', {'form': form})

   
# @login_required
# def List_Versement_Cle(request, pk):
#     versement =Versement.objects.get(id=pk)   

#     context = {
#           'versement':versement,
#           'id':pk
#       }
#     return render(request, 'versement/List_Versement_Cle.html',context)

@login_required
def Repartir_Montant(request):
    if request.method == 'POST' and 'montant' in request.POST and 'motif' in request.POST:
        montant = float(request.POST.get('montant', 0))
        motif = request.POST.get('motif', '')

        total_etats = Etat.objects.count()

        if total_etats > 0:
            quotient = montant / total_etats
            
            # Mettre à jour le champ cumAtt et motif dans chaque objet Etat
            for etat in Etat.objects.all():
                etat.cumAtt += quotient
                etat.motif = motif
                etat.save()

            return JsonResponse({'success': True, 'message': f'Montant réparti avec succès entre {total_etats} états.'})
        else:
            return JsonResponse({'success': False, 'message': 'Aucun état trouvé.'})
    else:
        return JsonResponse({'success': False, 'message': 'Montant ou motif non fourni.'})