from django.db import models


# Create your models here.

class Contact(models.Model):
    RELATIONSHIP_CHOICES = [
        ('FAMILY', 'Family'),
        ('FRIENDS', 'Friends'),
        ('RELATIVES', 'Relatives'),
        ('COWORKERS', 'Coworkers'),
        ('BUSINESS', 'Business')
    ]
    name: models.CharField = models.CharField(null=False)
    phone: models.IntegerField = models.IntegerField(blank=False, null=True)

    def __str__(self) -> str:
        if self.name == "":
            return self.phone
        return self.name