# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_of_show', models.DateTimeField(verbose_name='Дата показа баннера')),
                ('clicked', models.BooleanField(verbose_name='Было ли совершено нажатие?')),
                ('url_hash', models.CharField(max_length=255, verbose_name='HASH для формирования ссылки')),
            ],
            options={
                'verbose_name_plural': 'Активность: показы и клики',
                'verbose_name': 'Активность: показ и клик',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, help_text='Назовите баннер так, чтобы было удобно в дальнейшем определять его среди других баннеров', verbose_name='Название баннера')),
                ('file_swf', models.FileField(upload_to='data/', verbose_name='Swf-файл')),
                ('file_img', models.FileField(upload_to='data-img/', verbose_name='Файл изображения')),
                ('width', models.CharField(verbose_name='Ширина отображения баннера', max_length=7, blank=True, help_text='Например, 100px, 720px или 100%')),
                ('height', models.CharField(verbose_name='Высота отображения баннера', max_length=7, blank=True, help_text='Например, 100px, 200px или 100%')),
                ('link_to_1', models.CharField(max_length=255, help_text='Главная ссылка перехода. Передается параметром _clickTAG1. Например, http://vk.com/', verbose_name='Ссылка перехода #1')),
                ('link_to_2', models.CharField(verbose_name='Ссылка перехода #2', max_length=255, blank=True, help_text='Передается параметром _clickTAG2. Например, http://vk.com/')),
                ('link_to_3', models.CharField(verbose_name='Ссылка перехода #3', max_length=255, blank=True, help_text='Передается параметром _clickTAG3. Например, http://vk.com/')),
                ('link_to_4', models.CharField(verbose_name='Ссылка перехода #4', max_length=255, blank=True, help_text='Передается параметром _clickTAG4. Например, http://vk.com/')),
                ('date_from', models.DateField(default=datetime.datetime(2015, 2, 5, 10, 51, 32, 63828), verbose_name='Дата старта показа баннеров')),
                ('date_to', models.DateField(help_text='В эту дату ещё будут показы.', verbose_name='Дата окончания показа баннеров')),
                ('date_days', models.IntegerField(default=254, help_text='Вычисляется как сумма: Понедельник = 2, Вторник = 4, Среда = 8, Четверг = 16, Пятница = 32, Суббота = 64, Воскресенье = 128. Для всей недели = 254, Только выходные = 192, Только будни = 62', verbose_name='Дни недели для показа')),
                ('date_time_from', models.IntegerField(default=0, help_text='Например, 12 или 20', verbose_name='Час начала показа каждый указанный день')),
                ('date_time_to', models.IntegerField(default=24, help_text='Не может быть меньше, чем час начала. Например, 12 или 20', verbose_name='Час окончания показа каждый указанный день')),
                ('priority', models.IntegerField(verbose_name='Приоритет показа от 1 до 100')),
                ('limits', models.IntegerField(default=0, help_text='Баннер будет показывать заданное количество раз. Например, 1000', verbose_name='Ограничение по количеству показов')),
                ('limits_to_user', models.IntegerField(default=0, help_text='Пользователем считается каждый уникальный пользователь. 0 - без ограничений', verbose_name='Ограничение показов на пользователя')),
                ('targeting_tags', models.TextField(help_text='При вызове баннера вы можете передать теги для отображения. Например, чтобы показывать баннер только на страницах новостей вызовите на странице новостей баннер с параметром news, которые заносятся в это поле с новой строки.', verbose_name='Теги для отображения баннера')),
            ],
            options={
                'verbose_name_plural': 'Баннеры',
                'verbose_name': 'Баннер',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupTag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Название рубрик для тегов')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OutputTemplates',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Название шаблона')),
                ('template', models.TextField(help_text='HTML-код для вставки баннера. Поддерживаемые переменные - {{ url_swf }}, {{ url_img }}, {{ width }}, {{ height }}, {{ link_to_1 }}, {{ link_to_2 }}, {{ link_to_3 }}, {{ link_to_4 }} ', verbose_name='Шаблон')),
            ],
            options={
                'verbose_name_plural': 'Шаблоны',
                'verbose_name': 'Шаблон',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Место где будет размещатся банер')),
                ('code', models.TextField(verbose_name='Код размещения банер')),
                ('size', models.CharField(max_length=255, verbose_name='Размер размещаймого банера')),
            ],
            options={
                'verbose_name_plural': 'Расположение баннеров',
                'verbose_name': 'Расположение',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('last_visit', models.DateTimeField(verbose_name='Дата последнего визита')),
                ('ip', models.CharField(max_length=255, verbose_name='IP-адрес посетителя')),
                ('gender_male', models.BooleanField()),
                ('cookie', models.CharField(unique=True, max_length=255, verbose_name='Cookie')),
                ('from_user', models.CharField(max_length=255, verbose_name='Откуда пришол пользователь')),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
                'verbose_name': 'Пользователь',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='banner',
            name='position',
            field=models.ForeignKey(to='main.Position', verbose_name='Место размещение банера'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='banner',
            field=models.ForeignKey(to='main.Banner', verbose_name='Баннер'),
            preserve_default=True,
        ),
    ]
