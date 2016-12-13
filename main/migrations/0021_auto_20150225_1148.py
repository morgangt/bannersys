# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20150225_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertising',
            name='banner',
            field=models.ManyToManyField(to='main.Banner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rubrictag',
            name='desc',
            field=models.CharField(default='', verbose_name='Описание тега', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='date_from',
            field=models.DateField(default=datetime.datetime(2015, 2, 25, 11, 48, 41, 710112), verbose_name='Дата старта показа баннеров'),
            preserve_default=True,
        ),
    ]
