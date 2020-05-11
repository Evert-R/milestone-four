from django.db import models


# Create your models here.


class categories(models.Model):
    """
    Adding a category to the database
    Selectable in the category field in the work_items model
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def work_upload_dir(instance, filename):
    return "images/works/{}/{}".format(instance.work_item.id, filename)


class work_items(models.Model):
    """
    Adding a work to the database
    """
    main_image = models.ImageField(upload_to="images/works/")
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
        categories, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    under_title = models.CharField(max_length=50, blank=True)
    free_text = models.CharField(max_length=3000, blank=True)
    work_item = models.BooleanField(default=True, blank=True)
    shop_item = models.BooleanField(default=False, blank=True)
    shop_settings = models.OneToOneField(
        'shop.shop_items', on_delete=models.SET_NULL, blank=True, null=True)
    sort_order = models.SmallIntegerField(default=999)

    def __str__(self):
        return self.title


class work_images(models.Model):
    """
    Extra work images
    """
    work_item = models.ForeignKey(
        'works.work_items', on_delete=models.CASCADE, null=True)
    work_image = models.ImageField(upload_to=work_upload_dir)
    sort_order = models.SmallIntegerField(default=999)
