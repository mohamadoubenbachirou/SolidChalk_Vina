from django import forms
from django.forms import ModelForm
#from .models import Manages_files
from django import forms
from .models import UserLanguage

# class FormManage_file(ModelForm):
#     class Meta:
#         model=Manages_files
#         fields="__all__"

class Upload_File_Form(forms.Form):
    title=forms.CharField(max_length=255)
    File=forms.FileField()

class LanguageForm(forms.ModelForm):
    class Meta:
        model = UserLanguage
        fields = ['language']
