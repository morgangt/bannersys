# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150211_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_from',
            field=models.DateField(default=datetime.datetime(2015, 2, 13, 14, 9, 36, 871014), verbose_name='Дата старта показа баннеров'),
            preserve_default=True,
        ),
    ]
