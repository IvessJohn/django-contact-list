"""Contains the project's models."""
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(models.Model):
    """A model associated with the User. Every Customer has its own list of Contacts (one-to-many relationship)"""

    user: models.OneToOneField = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    name: models.CharField = models.CharField(max_length=96, null=True)

    def __str__(self) -> str:
        if self.name == "":
            return f"Customer {self.id}"
        return self.name


class Contact(models.Model):
    """A model with contact info. Every Contact is associated with only one Customer at a time."""

    class Relationship(models.TextChoices):
        FAMILY = "FAMILY", _("Family")
        FRIENDS = "FRIENDS", _("Friends")
        RELATIVES = "RELATIVES", _("Relatives")
        COWORKERS = "COWORKERS", _("Coworkers")
        BUSINESS = "BUSINESS", _("Business")

    contact_owner: models.ForeignKey = models.ForeignKey(
        Customer, null=True, on_delete=models.DO_NOTHING
    )
    phone: PhoneNumberField = PhoneNumberField(blank=False, null=False, unique=True)
    name: models.CharField = models.CharField(max_length=96, null=False)
    email: models.EmailField = models.EmailField(
        max_length=96, blank=True, null=False, unique=False, help_text="Contact's email"
    )
    relationship: models.CharField = models.CharField(
        max_length=48, blank=True, choices=Relationship.choices
    )
    address: models.CharField = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        if self.name == "":
            return self.phone
        return self.name
