from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Contact


# Contact creation/editing form
class ContactForm(ModelForm):
    """A form for creating and editing contact information."""

    class Meta:
        model = Contact
        fields = "__all__"
        exceptions = ['contact_owner']


class RegisterForm(UserCreationForm):
    """A custom form for user creation."""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        exclude = []