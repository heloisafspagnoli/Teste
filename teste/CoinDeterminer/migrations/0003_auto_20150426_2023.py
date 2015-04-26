# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoinDeterminer', '0002_auto_20150426_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='descriptionmodel',
            options={'verbose_name_plural': 'Description'},
        ),
    ]
