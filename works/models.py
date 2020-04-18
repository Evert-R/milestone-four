from django.db import models
import datetime

# Create your models here.


class categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class work_types(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class materials(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class work_sizes(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class work_items(models.Model):
    main_image = models.ImageField(upload_to='images')
    HORIZONTAL = 'HZ'
    VERTICAL = 'VT'
    POSITION_CHOICES = [
        (HORIZONTAL, 'Horizontal'),
        (VERTICAL, 'Vertical')
    ]
    position = models.CharField(max_length=2,
                                choices=POSITION_CHOICES,
                                default=VERTICAL)
    category = models.ForeignKey(
        categories, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    under_title = models.CharField(max_length=50, blank=True)
    free_text = models.CharField(max_length=3000, blank=True)
    work_item = models.BooleanField(default=True, blank=True)
    shop_item = models.BooleanField(default=False, blank=True)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    stock = models.SmallIntegerField(blank=True, null=True)
    edition_count = models.SmallIntegerField(blank=True, null=True)
    frame = models.BooleanField(default=False, blank=True)
    signed = models.BooleanField(default=True, blank=True)
    date_modified = models.DateField(auto_now=True)
    work_type = models.ForeignKey(
        work_types, on_delete=models.CASCADE, blank=True, null=True)
    material = models.ForeignKey(
        materials, on_delete=models.CASCADE, blank=True, null=True)
    work_size = models.ForeignKey(
        work_sizes, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
