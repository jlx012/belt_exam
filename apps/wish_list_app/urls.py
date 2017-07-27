from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create$', views.create, name='create-item'),
    url(r'^createpage$', views.createPage, name='wish-page'),
    url(r'^', views.index),
]
