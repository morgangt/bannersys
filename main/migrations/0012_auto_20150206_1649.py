# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150205_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_from',
            field=models.DateField(verbose_name='Дата старта показа баннеров', default=datetime.datetime(2015, 2, 6, 16, 49, 30, 274457)),
            preserve_default=True,
        ),
    ]
