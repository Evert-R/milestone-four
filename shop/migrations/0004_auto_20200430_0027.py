# Generated by Django 3.0.5 on 2020-04-29 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200430_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_items',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.materials'),
        ),
        migrations.AlterField(
            model_name='shop_items',
            name='work_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.work_sizes'),
        ),
        migrations.AlterField(
            model_name='shop_items',
            name='work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.work_types'),
        ),
    ]