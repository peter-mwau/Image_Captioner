from django.forms import ModelForm
from django import forms
# from django.db import models  
# from django.forms import fields  
from .models import UploadImage 




  
class UserImage(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form 
        model = UploadImage
        # It includes all the fields of model  
        fields = '__all__'  

   
    

# class Caption(forms.Form):
#     caption = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder': ' Output'}))





