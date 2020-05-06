from django.db import models
from django.contrib.auth.models import User
from works.models import work_items

# Create your models here.


class orders(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    total = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)
    address1 = models.CharField(blank=True, max_length=50)
    address2 = models.CharField(blank=True, max_length=50)
    postcode = models.CharField(blank=True, max_length=50)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    telephone = models.CharField(blank=True, max_length=25)
    shipping = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.user.last_name)


class order_items(models.Model):
    order = models.ForeignKey(orders, null=False, on_delete=models.CASCADE)
    work_item = models.ForeignKey(
        work_items, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.work_item.title, self.work_item.shop_settings.price)
