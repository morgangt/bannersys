# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150209_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='activ',
            field=models.BooleanField(verbose_name='Активность баннера', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='date_from',
            field=models.DateField(verbose_name='Дата старта показа баннеров', default=datetime.datetime(2015, 2, 11, 9, 23, 39, 301497)),
            preserve_default=True,
        ),
    ]
