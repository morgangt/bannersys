# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20150225_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertising',
            options={'verbose_name_plural': 'Рекламные кампании', 'verbose_name': 'Рекламая кампания'},
        ),
        migrations.AlterModelOptions(
            name='rubrictag',
            options={'verbose_name_plural': 'Рубрики тегов', 'verbose_name': 'Рубрика тега'},
        ),
        migrations.AlterModelOptions(
            name='tages',
            options={'verbose_name_plural': 'Теги', 'verbose_name': 'Тег'},
        ),
        migrations.AlterField(
            model_name='advertising',
            name='banner',
            field=models.ManyToManyField(to='main.Banner', verbose_name='Банер'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='banner',
            name='date_from',
            field=models.DateField(default=datetime.datetime(2015, 2, 25, 13, 36, 0, 390640), verbose_name='Дата старта показа баннеров'),
            preserve_default=True,
        ),
    ]
