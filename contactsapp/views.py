"""Contains the project views."""
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Customer, Contact
from .forms import ContactForm, RegisterForm
from .filters import ContactFilter
from .decorators import unauthenticated_user

# Create your views here.
# region AUTHENTICATION VIEWS
@unauthenticated_user
def register_view(request):
    register_form: RegisterForm = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user: User = register_form.save()
            username: str = user.username

            Customer.objects.create(user=user, name=username)

            messages.info(request, f"User {username} was created successfully!")

            return redirect("login")

    context = {"register_form": register_form}
    return render(request, "contactsapp/auth_register.html", context)


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        _username: str = request.POST.get("username")
        _password: str = request.POST.get("password")

        user: User = authenticate(request.POST, username=_username, password=_password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect.")

    context = {}
    return render(request, "contactsapp/auth_login.html", context)


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")


# endregion


@login_required(login_url="login")
def about(request):
    """The About page's view. Just some info, nothing special."""
    return render(request, "contactsapp/about.html")


# region CONTACT LIST VIEWS
@login_required(login_url="login")
def home(request):
    """The main page's view, where the contact list is shown."""
    contact_owner: Customer = Customer.objects.get(user=request.user)
    contacts = contact_owner.contact_set.all()

    contact_amount = contacts.count()
    contactFilter = ContactFilter(request.GET, queryset=contacts)
    contacts = contactFilter.qs

    context = {
        "contacts": contacts,
        "contact_amount": contact_amount,
        "contactFilter": contactFilter,
    }
    return render(request, "contactsapp/home.html", context)


@login_required(login_url="login")
def contact_add(request):
    """A view for adding a new contact."""
    owner: Customer = request.user.customer

    contact_form: ContactForm = ContactForm(
        initial={"contact_owner": request.user.customer}
    )

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # Create a new contact by receiving data from the form
            new_contact: Contact = contact_form.save()

            # Assign the contact's contact owner (the form excludes this field)
            new_contact.contact_owner = owner

            new_contact.save()

            return redirect("contact_info", contact_id=new_contact.id)
        else:
            print(messages.get_messages(request))

    context = {"contact_form": contact_form, "is_adding_a_contact": True}
    return render(request, "contactsapp/contact_edit.html", context)


@login_required(login_url="login")
def contact_info(request, contact_id: int):
    """A view for the contact's information page."""
    contact = Contact.objects.get(id=contact_id)

    context = {"contact": contact}
    return render(request, "contactsapp/contact_info.html", context)


@login_required(login_url="login")
def contact_edit(request, contact_id: int):
    """A view for editing an existing contact's information."""

    contact: Contact = Contact.objects.get(id=contact_id)
    contact_form: ContactForm = ContactForm(instance=contact)

    if request.method == "POST":
        contact_form = ContactForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("contact_info", contact_id=contact.id)

    context = {
        "contact": contact,
        "contact_form": contact_form,
        "is_adding_a_contact": False,
    }
    return render(request, "contactsapp/contact_edit.html", context)


@login_required(login_url="login")
def contact_delete(request, contact_id: int):
    """A view for editing an existing contact's information."""

    contact: Contact = Contact.objects.get(id=contact_id)

    if request.method == "POST":
        contact.delete()
        return redirect("home")

    context = {
        "contact": contact
    }
    return render(request, "contactsapp/contact_delete.html", context)


# endregion
