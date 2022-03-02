from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, Group

from .models import Customer, Contact
from .filters import ContactFilter

# Create your views here.
def home(request):
    """The main page's view, where the contact list is shown."""
    contacts = Contact.objects.all()

    contactFilter = ContactFilter(request.GET, queryset=contacts)
    contacts = contactFilter.qs

    context = {"contacts": contacts, "contactFilter": contactFilter}
    return render(request, "contactsapp/home.html", context)


def about(request):
    """The About page's view. Just some info, nothing special."""
    return render(request, "contactsapp/about.html")


def contact_add(request, contact_id: int):
    context = {}
    return render(request, "contactsapp/contact_add.html", context)


def contact_info(request, contact_id: int):
    contact = Contact.objects.get(id=contact_id)

    context = {"contact": contact}
    return render(request, "contactsapp/contact_info.html", context)
