from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    # Authentication
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    # Main functionality
    path("", views.home, name="home"),
    path("contact/add/", views.contact_add, name="contact_add"),
    path("contact/<str:contact_id>/info/", views.contact_info, name="contact_info"),
    path("contact/<str:contact_id>/edit/", views.contact_edit, name="contact_edit"),
    path("contact/<str:contact_id>/delete/", views.contact_delete, name="contact_delete"),
    # Extras
    path("about/", views.about, name="about"),
]
