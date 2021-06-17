from django.conf.urls import url

from . import views

app_name = 'news'

urlpatterns = [
    url('', views.index, name='index'),
    url('news/contact', views.contact, name='contact')
]
