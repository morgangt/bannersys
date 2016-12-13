# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150205_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(default='', to='main.UserBase', verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='date_from',
            field=models.DateField(verbose_name='Дата старта показа баннеров', default=datetime.datetime(2015, 2, 5, 11, 11, 55, 642778)),
            preserve_default=True,
        ),
    ]
