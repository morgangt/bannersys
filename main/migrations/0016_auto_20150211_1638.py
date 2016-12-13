# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20150211_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_from',
            field=models.DateField(default=datetime.datetime(2015, 2, 11, 16, 38, 13, 440158), verbose_name='Дата старта показа баннеров'),
            preserve_default=True,
        ),
    ]
