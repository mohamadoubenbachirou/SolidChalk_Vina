from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreerUtilisateur
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='acces')
def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=="POST":
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acces')
    context={'form':form}
    return render(request, 'compte/inscription.html', context)

#@login_required(login_url='acces')
# def accesPage(request):
#     context={}
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         User=authenticate(request,username=username,password=password)
#         if User is not None:
#             login(request,User)
#             return redirect('accueil')
#         else:
#             messages.info(request, "Il y a une erreur dans le nom d'utilisateur et/ou le mot de passe")
#             #user=form.cleaned_data.get('username')
#     return render(request, 'compte/acces.html', context)


def accesPage(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Stocke le nom d'utilisateur dans la session
            request.session['username'] = username
            request.session['password'] = password

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