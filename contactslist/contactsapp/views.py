from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, Group

from .models import Customer, Contact
from .forms import ContactForm
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


def contact_add(request):
    """A view for adding a new contact."""

    is_adding_a_contact: bool = True
    contact_form: ContactForm = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("/")

    context = {"contact_form": contact_form, "is_adding_a_contact": is_adding_a_contact}
    return render(request, "contactsapp/contact_edit.html", context)


def contact_info(request, contact_id: int):
    contact = Contact.objects.get(id=contact_id)

    context = {"contact": contact}
    return render(request, "contactsapp/contact_info.html", context)


def contact_edit(request, contact_id: int):
    """A view for editing an existing contact's information."""

    is_adding_a_contact: bool = False
    contact: Contact = Contact.objects.get(id=contact_id)
    contact_form: ContactForm = ContactForm(instance=contact)

    if request.method == "POST":
        contact_form = ContactForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("/")

    context = {"contact_form": contact_form, "is_adding_a_contact": is_adding_a_contact}
    return render(request, "contactsapp/contact_edit.html", context)
