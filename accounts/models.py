from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class user_details(models.Model):
    """
    Adding a work to the database
    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    telephone = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.user.username
