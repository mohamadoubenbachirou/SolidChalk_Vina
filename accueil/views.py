from django.shortcuts import render, redirect
from django.http import FileResponse
from membre.models import Membre
from etat.models import Etat
from post.models import Post
from versement.models import Versement
from django.contrib.auth.decorators import login_required
from django.utils.translation import activate
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from profil.models import UserProfile
from .forms import LanguageForm
from django.utils import translation
# from .forms import FormManage_file
# from .models import Manages_files
# import fitz
# from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.

@login_required
def home(request):
   membres=Membre.objects.all()
   total_membre = Membre.objects.count()
   etats=Etat.objects.all()
   total_etat = Etat.objects.count()
   posts=Post.objects.all()
   total_post = Post.objects.count()
   versements=Versement.objects.all()
   total_versement = Versement.objects.count()
   if request.user.is_authenticated:
      user_profile, Create = UserProfile.objects.get_or_create(user=request.user)
      user_profile.last_activity = timezone.now()
      user_profile.save()
      online_users_count = UserProfile.objects.filter(last_activity__gte=timezone.now() - timedelta(minutes=1)).count()
   context={'online_users_count': online_users_count, 'membres':membres, 'total_membre': total_membre,'etats':etats, 'total_etat': total_etat, 'posts':posts, 'total_post': total_post, 'versements':versements, 'total_versement': total_versement,}
   return render(request, 'accueil/accueil.html', context,)

@login_required
def recherche(request):
    if request.method == "POST":
        recherche = request.POST['recherche']
        membres=Membre.objects.filter(nom__contains=recherche)
        etats=Etat.objects.filter(cumVers__contains=recherche)
        posts=Post.objects.filter(objet__contains=recherche)
        versements=Versement.objects.filter(montant__contains=recherche)
        context = {
            'recherche': recherche, 'membres':membres, 'etats':etats, 'posts':posts, 'versements':versements
            }

        return render(request, 'accueil/recherche.html', context)
    else:
        return render(request, 'accueil/recherche.html', context)

@login_required
def List_Membre(request): 
   liste_membre = Membre.objects.all()
   
   context = {
      "membre" : liste_membre,
      
      }
   return render(request, 'membre/List_Membre.html',context)

@login_required
def List_Versement(request):
   liste_versement = Versement.objects.all()
   
   context = {
      "versement" : liste_versement,
      
      }
   return render(request, 'versement/List_Versement.html', context)

@login_required
def List_Etat(request):
   liste_etat = Etat.objects.all()
   
   context = {
      "etat" : liste_etat,
      
      }
   return render(request, 'etat/List_Etat.html', context)

@login_required
def List_Post(request):
   liste_post = Post.objects.all()
   
   context = {
      "post" : liste_post,
      

      }
   return render(request,'post/List_Post.html', context)

#def change_language(request, language):
#   activate(language)
#   return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def change_language(request):
    if 'language' in request.GET:
        language = request.GET['language']
        translation.activate(language)
        request.session['django_language'] = language
        print(f"Langue changée en : {language}")
    
    next_url = request.GET.get('next', '/')
    print(f"Redirection vers : {next_url}")
    
    full_path = request.get_full_path()
    print(f"URL générée : {full_path}")

    return redirect(next_url)

   # def ouvrir_pdf(request,pk):
#    nbr = 0
#    erreur = ""
#    link = Manages_files.objects.get(id=pk)
#    chemin = link.file
   
#    try:
#       document = fitz.open(chemin)
#       nbr = document.page_count
#       bs = document
#       pages = ["1"]*nbr
#       for i in range(nbr):
#          pages[i] = document[i].get_text()
#       document.close()
#    except Exception as e:
#       erreur = str(e)
#    paginator = Paginator(pages,1)
#    page = request.GET.get('page')
   
#    try:
#       object_page = paginator.page(page)
#    except PageNotAnInteger:
#       object_page = paginator.page(1)
#    except EmptyPage:
#       object_page = paginator.page(paginator.num_pages)
#    context = {'tab':object_page,'doc': page,"document" : pages ,"erreur":erreur,"nbr":nbr}
#    return render(request,"accueil/pdf.html",context)

