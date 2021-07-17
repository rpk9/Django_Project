from django import forms
from . models import SignUp


class SignUpForm(forms.ModelForm):
    Password = forms.CharField(max_length=8,widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(max_length=8,widget=forms.PasswordInput)
    class Meta():
        model = SignUp
        fields = '__all__'

class LogInForm(forms.ModelForm):
    Password=forms.CharField(max_length=8,widget=forms.PasswordInput)
    class Meta():
        model = SignUp
        fields = ['Email','Password']
        
class UpdateForm(forms.ModelForm):
    #Password=forms.CharField(max_length=8,widget=forms.PasswordInput)
    class Meta():
        model = SignUp
        fields = ['Name','Email','Age','Photo']        
        
        
class ChangePasswordForm(forms.Form):
    #Password=forms.CharField(max_length=8,widget=forms.PasswordInput)
    #class Meta():
        #model = SignUp
        #fields = ['Name','Email','Age','Photo']
    OldPassword = forms.CharField(max_length=8,widget=forms.PasswordInput)
    NewPassword = forms.CharField(max_length=8,widget=forms.PasswordInput)
    ConfirmNewPassword = forms.CharField(max_length=8,widget=forms.PasswordInput)
             