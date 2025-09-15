
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from wscubetech import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('services/', views.services, name="services"),
    path('collections/', views.collections, name="collections"),
    path('contact/', views.contact, name="contact"),
]

