# Generated by Django 3.0.5 on 2020-05-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]