from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.booking, name='home'),
    path("booking", views.booking, name='booking'), 
]