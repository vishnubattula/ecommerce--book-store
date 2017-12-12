# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='SKU',
            field=models.CharField(default=datetime.datetime(2017, 12, 2, 13, 28, 34, 297293, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
