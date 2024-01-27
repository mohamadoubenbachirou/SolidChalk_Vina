from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PosterForm
from django.contrib import messages
from .filters import PostFiltre

# Create your views here.
@login_required
def List_Post(request):
   liste_post = Post.objects.all()
   total_post = Post.objects.count()
   myFilter = PostFiltre(request.GET, queryset=liste_post)
   liste_post=myFilter.qs
   context = {
      "post" : liste_post,
      'total_post': total_post,
      'myFilter':myFilter,

      }
   return render(request,'post/List_Post.html', context)

# @login_required
# def Ajouter_Post(request):
#    form=PostForm()
#    if request.method=='POST':
#       form=PostForm(request.POST)
#       if form.is_valid():
#          form.save()
#          return redirect('accueil')
#    context={'form':form}
#    return render(request, 'post/Ajouter_Post.html', context)

# @login_required
# def Modifier_Post(request,pk):
#    post=Post.objects.get(id=pk)
#    form=PostForm(instance=post)

#    if request.method=='POST':
#       form=PostForm(request.POST, instance=post)
#       if form.is_valid():
#          form.save()
#          return redirect('accueil')
#    context={'form':form}
#    return render(request, 'post/Ajouter_Post.html', context)

# @login_required
# def Supprimer_Post(request,pk):
#    post=Post.objects.get(id=pk)
#    if request.method=='POST':
#       post.delete()
#       return redirect('accueil')
#    context={'item':post}
#    return render(request, 'post/Supprimer_Post.html', context)

# @login_required
# def Poster(request):
#    form = PosterForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = PosterForm()
#        return redirect('accueil')
#    return render(request, 'post/Poster.html', {'form':form})

# @login_required
# def List_Post_Cle(request, pk):
#     post =Post.objects.get(id=pk)   

#     context = {
#           'post':post,
#           'id':pk
#       }
#     return render(request, 'post/List_Post_Cle.html',context)
