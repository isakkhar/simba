from django.shortcuts import render
from django.urls import path

from Junior import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
