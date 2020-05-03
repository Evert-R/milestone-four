from django.db import models
from django.contrib.auth.models import User
from shop.models import shipping

# Create your models here.


class user_details(models.Model):
    """
    Adding user details to the database
    """

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    telephone = models.CharField(max_length=25, blank=True)
    shipping = models.ForeignKey(
        shipping, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
