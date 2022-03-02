from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, Group

from .models import Customer, Contact

# Create your views here.
def home(request):
    contacts = Contact.objects.all()

    # SEARCH FORM HERE
    #
    #

    context = {'contacts': contacts}
    return render(request, 'contactsapp/main.html', context)

def about(request):
    return render(request, 'contactsapp/about.html')

def contact_info(request, contact_id: int):
    context = {}
    return render(request, 'contactsapp/contact_info.html', context)