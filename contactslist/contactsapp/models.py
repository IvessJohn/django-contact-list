from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(models.Model):
    """A model associated with the User. Every Customer has its own list of Contacts (one-to-many relationship)"""

    user: models.OneToOneField = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE
    )


class Contact(models.Model):
    """A model with contact info. Every Contact is associated with only one Customer at a time."""

    RELATIONSHIP_CHOICES = [
        ("FAMILY", "Family"),
        ("FRIENDS", "Friends"),
        ("RELATIVES", "Relatives"),
        ("COWORKERS", "Coworkers"),
        ("BUSINESS", "Business")
    ]
    phone: IntegerField = IntegerField(
        blank=False, null=True, unique=True
    )
    name: models.CharField = models.CharField(max_length=96, null=False)
    email: models.CharField = models.CharField(
        max_length=96, blank=True, null=False, unique=False
    )
    relationship: models.CharField = models.CharField(
        max_length=48, choices=RELATIONSHIP_CHOICES
    )

    def __str__(self) -> str:
        if self.name == "":
            return self.phone
        return self.name
