from django.forms import ModelForm
from .models import Post
from django import forms

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['objet' ,'texte', 'date']

class PosterForm(forms.ModelForm):
    class Meta:
         model = Post
         fields=['membre', 'objet' ,'texte', 'date']