from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/add/', views.contact_add, name='contact_add'),
    path('contact/<str:contact_id>/info/', views.contact_info, name='contact_info'),
    path('contact/<str:contact_id>/edit/', views.contact_edit, name='contact_edit'),
]