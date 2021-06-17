from django.contrib import admin
from .models import User, Post, Comment

my_models = [User, Post, Comment]

admin.site.register(my_models)