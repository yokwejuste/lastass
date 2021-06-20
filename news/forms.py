from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User 
from django.forms import ModelForm
from django import forms
from news.models import Post, Comment

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput
#         }


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=20) 
    password = forms.CharField(label='Password', widget=forms.PasswordInput , max_length=20) 


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']