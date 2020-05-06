from django.db import models
from django.contrib.auth.models import User
from checkout.models import orders

# Create your models here.


class work_types(models.Model):
    """
    Adding a work type to the database
    Selectable in the work_type field in the work_items model
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class materials(models.Model):
    """
    Adding a material to the database
    Selectable in the material field in the work_items model
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class work_sizes(models.Model):
    """
    Adding a work size to the database
    Selectable in the work_size field in the work_items model 
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class shipping(models.Model):
    """
    Shipping cost per region
    """
    region = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.region


class reviews(models.Model):
    """
    Reviews for ordered items
    """
    free_text = models.CharField(max_length=3000, blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    order = models.OneToOneField(orders, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class shop_items(models.Model):
    """
    Adding a work to the database
    """

    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)
    stock = models.SmallIntegerField(default=0)
    edition_count = models.SmallIntegerField(default=0)
    FRAME = 'FR'
    NOFRAME = 'NF'
    FRAME_CHOICES = [
        (FRAME, 'Frame'),
        (NOFRAME, 'No Frame'),
    ]
    frame = models.CharField(max_length=2,
                             choices=FRAME_CHOICES,
                             blank=True,
                             null=True)
    signed = models.BooleanField(default=True)
    date_modified = models.DateField(auto_now=True)
    work_type = models.ForeignKey(
        work_types, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(
        materials, on_delete=models.SET_NULL, null=True)
    work_size = models.ForeignKey(
        work_sizes, on_delete=models.SET_NULL, null=True)
    personal_message = models.CharField(max_length=200, blank=True)
    personal_text = models.BooleanField(default=False)
    standard_text = models.BooleanField(default=True)
    sort_order = models.SmallIntegerField(default=999)
