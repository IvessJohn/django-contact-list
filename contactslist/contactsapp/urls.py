from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/<str:contact_id>', views.home, name='contact_info'),
]