from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect,get_object_or_404
from news.forms import LoginForm, SignUpForm
from news.models import User, Post

# SPECIAL:CASE: password hash
import hashlib
import os



def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }       
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    
    # form = UserForm()
    user = User()
    form = SignUpForm()
    error = ''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            emailid = form.cleaned_data['email']
            name = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            # password = form.cleaned_data['password1']
            if (User.objects.filter(email=emailid)):
                error = 'Email has already exist'
            else:
                salt = os.urandom(32) # A new salt for this user
                key = hashlib.pbkdf2_hmac('sha256', password1.encode('utf-8'), salt, 100000)
                user.name = name
                user.password = password1
                user.email = emailid
                
                user.save()
                return HttpResponseRedirect(reverse("news:success"))
        else:
            form = SignUpForm()
    
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'signup.html', context)


def loginPage(request):
    user = User()
    form = LoginForm()
    email = ''
    error = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if User.objects.filter(email=email, password=password):
                userAuth = authenticate(request, email=email, password=password)
                return HttpResponseRedirect(reverse("news:index"))
                if userAuth is not None:
                    login(request, userAuth)
                    request.session['email'] = email
                    return HttpResponseRedirect(reverse("news:index"))

            else:
                error = 'Error loggin in'
                return HttpResponseRedirect('Could not login')
            
        else:
            form = LoginForm()
    context = {
        'form': form,
        'email':email,
        'error': error
    }
    return render(request, 'login.html', context)

def success(request):
    return render(request, 'success.html')

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('news:index'))

def create(request):
    if(request) is not None:
        return render(request, 'create.html')
    else:
        return HttpResponseRedirect(reverse('news:index'))