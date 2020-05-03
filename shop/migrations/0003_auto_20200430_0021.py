# Generated by Django 3.0.5 on 2020-04-29 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop_items_sort_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_items',
            name='personal_message',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='shop_items',
            name='edition_count',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shop_items',
            name='frame',
            field=models.CharField(blank=True, choices=[('FR', 'Frame'), ('NF', 'No Frame')], max_length=2, null=True),
        ),
    ]