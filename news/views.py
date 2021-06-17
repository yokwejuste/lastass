from django.shortcuts import render
# from django.forms import Forms

# class Contact(Forms):
#     name = ''

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')
