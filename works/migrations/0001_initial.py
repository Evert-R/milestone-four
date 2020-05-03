# Generated by Django 3.0.5 on 2020-05-03 14:57

from django.db import migrations, models
import django.db.models.deletion
import works.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='work_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(upload_to='images/works/')),
                ('position', models.CharField(choices=[('HZ', 'Horizontal'), ('VT', 'Vertical')], default='VT', max_length=2)),
                ('title', models.CharField(max_length=50)),
                ('under_title', models.CharField(blank=True, max_length=50)),
                ('free_text', models.CharField(blank=True, max_length=3000)),
                ('work_item', models.BooleanField(blank=True, default=True)),
                ('shop_item', models.BooleanField(blank=True, default=False)),
                ('sort_order', models.SmallIntegerField(default=0)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='works.categories')),
                ('shop_settings', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.shop_items')),
            ],
        ),
        migrations.CreateModel(
            name='work_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_image', models.ImageField(upload_to=works.models.work_upload_dir)),
                ('work_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='works.work_items')),
            ],
        ),
    ]
