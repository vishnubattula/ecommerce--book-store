# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
