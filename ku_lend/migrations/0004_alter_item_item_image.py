# Generated by Django 3.2.9 on 2021-11-06 08:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ku_lend', '0003_alter_history_borrower_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]