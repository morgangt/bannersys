# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150205_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='date_from',
            field=models.DateField(default=datetime.datetime(2015, 2, 5, 10, 51, 56, 53864), verbose_name='Дата старта показа баннеров'),
            preserve_default=True,
        ),
    ]
