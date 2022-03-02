from django import forms
from django.forms import ModelForm

from .models import Contact


# Contact creation/editing form
class ContactForm(ModelForm):
    """A form for creating and editing contact information."""

    class Meta:
        model = Contact
        fields = "__all__"
        exceptions = []
