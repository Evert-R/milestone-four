from django.db import models

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


class shop_items(models.Model):
    """
    Adding a work to the database
    """

    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)
    stock = models.SmallIntegerField(default=0)
    edition_count = models.SmallIntegerField(blank=True, null=True)
    frame = models.BooleanField(default=False)
    signed = models.BooleanField(default=True)
    date_modified = models.DateField(auto_now=True)
    work_type = models.ForeignKey(
        work_types, on_delete=models.CASCADE, blank=True, null=True)
    material = models.ForeignKey(
        materials, on_delete=models.CASCADE, blank=True, null=True)
    work_size = models.ForeignKey(
        work_sizes, on_delete=models.CASCADE, blank=True, null=True)
