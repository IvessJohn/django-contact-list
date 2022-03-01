from django.db import models


# Create your models here.


class Customer(models.Model):
    """A model associated with the User. Every Customer has its own list of Contacts (one-to-many relationship)"""

    pass


class Contact(models.Model):
    """A model with contact info. Every Contact is associated with only one Customer at a time."""

    RELATIONSHIP_CHOICES = [
        ("FAMILY", "Family"),
        ("FRIENDS", "Friends"),
        ("RELATIVES", "Relatives"),
        ("COWORKERS", "Coworkers"),
        ("BUSINESS", "Business"),
    ]
    name: models.CharField = models.CharField(null=False)
    phone: models.IntegerField = models.IntegerField(blank=False, null=True)

    def __str__(self) -> str:
        if self.name == "":
            return self.phone
        return self.name
