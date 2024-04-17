from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    mail_address = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    class Meta:
        model = Users
        fields = ("mail_address", "password")
        

class ServiceCenterForm(forms.ModelForm):
    mail_address = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    class Meta:
        model = Users
        fields = ("mail_address", "password")