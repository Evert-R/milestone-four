# Generated by Django 3.0.5 on 2020-05-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_orders_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_items',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]