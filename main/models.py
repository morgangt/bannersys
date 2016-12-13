from django.db import models
from datetime import *
from django.contrib.auth.models import Group
from django.conf import settings

class GroupTag(models.Model): ##рубрика тега
	name = models.CharField(max_length=255,blank=False, verbose_name="Название рубрик для тегов")

class OutputTemplates(models.Model): ##шаблоны для показа бенера
    name = models.CharField(max_length=256, blank=False, verbose_name='Название шаблона')
    template = models.TextField(blank=False, verbose_name='Шаблон', help_text='HTML-код для вставки баннера. Поддерживаемые переменные - {{ url_swf }}, {{ url_img }}, {{ width }}, {{ height }}, {{ link_to_1 }}, {{ link_to_2 }}, {{ link_to_3 }}, {{ link_to_4 }} ')
    def __str__(self):
        return u'Шаблон %s' % (self.name)

    class Meta:
        verbose_name = "Шаблон"
        verbose_name_plural = "Шаблоны"

class Position(models.Model):
	name = models.CharField(max_length=255, verbose_name='Место где будет размещатся банер')
	code = models.TextField(verbose_name='Код размещения банер')
	size = models.CharField(max_length=255, verbose_name='Размер размещаймого банера')
	#template = models.ForeignKey(OutputTemplates, verbose_name='Шаблон для этого места')
	
	def __str__(self):
		return u'Расположение %s' % (self.name)

	class Meta:
		verbose_name = "Расположение"
		verbose_name_plural = "Расположение баннеров"

class Banner(models.Model): ##банера
	name = models.CharField(max_length=255, blank=False, verbose_name='Название баннера', help_text='Назовите баннер так, чтобы было удобно в дальнейшем определять его среди других баннеров')
	file_swf = models.FileField(upload_to='data/', verbose_name='Swf-файл')
	file_img = models.FileField(upload_to='data-img/', verbose_name='Файл изображения')
	width = models.CharField(max_length=7, blank=True, verbose_name='Ширина отображения баннера', help_text='Например, 100px, 720px или 100%')
	height = models.CharField(max_length=7, blank=True, verbose_name='Высота отображения баннера', help_text='Например, 100px, 200px или 100%')
	link_to_1 = models.CharField(max_length=255, blank=False, verbose_name='Ссылка перехода #1', help_text='Главная ссылка перехода. Передается параметром _clickTAG1. Например, http://vk.com/')
	link_to_2 = models.CharField(max_length=255, blank=True, verbose_name='Ссылка перехода #2', help_text='Передается параметром _clickTAG2. Например, http://vk.com/')
	link_to_3 = models.CharField(max_length=255, blank=True, verbose_name='Ссылка перехода #3', help_text='Передается параметром _clickTAG3. Например, http://vk.com/')
	link_to_4 = models.CharField(max_length=255, blank=True, verbose_name='Ссылка перехода #4', help_text='Передается параметром _clickTAG4. Например, http://vk.com/')
	date_from = models.DateField(default=datetime.now(), verbose_name='Дата старта показа баннеров', help_text='')
	date_to = models.DateField(verbose_name='Дата окончания показа баннеров', help_text='В эту дату ещё будут показы.')
	date_days = models.IntegerField(default=254, verbose_name='Дни недели для показа', help_text='Вычисляется как сумма: Понедельник = 2, Вторник = 4, Среда = 8, Четверг = 16, Пятница = 32, Суббота = 64, Воскресенье = 128. Для всей недели = 254, Только выходные = 192, Только будни = 62')
	date_time_from = models.IntegerField(default=0, verbose_name='Час начала показа каждый указанный день' , help_text='Например, 12 или 20')
	date_time_to = models.IntegerField(default=24, verbose_name='Час окончания показа каждый указанный день' , help_text='Не может быть меньше, чем час начала. Например, 12 или 20')
	priority = models.IntegerField(verbose_name='Приоритет показа от 1 до 100' , help_text='')
	limits = models.IntegerField(blank=False, default=0, verbose_name='Ограничение по количеству показов', help_text='Баннер будет показывать заданное количество раз. Например, 1000')
	limits_to_user = models.IntegerField(default=0, verbose_name='Ограничение показов на пользователя' , help_text='Пользователем считается каждый уникальный пользователь. 0 - без ограничений')
	targeting_tags = models.TextField(blank=False, verbose_name='Теги для отображения баннера', help_text='При вызове баннера вы можете передать теги для отображения. Например, чтобы показывать баннер только на страницах новостей вызовите на странице новостей баннер с параметром news, которые заносятся в это поле с новой строки.')
	position = models.ForeignKey(Position, verbose_name='Место размещение банера')
	activ = models.BooleanField(verbose_name='Активность баннера')
	
	def __str__(self):
		return u'Баннер %s' % (self.name)

	def showed(obj):
		return '%s/%s' % (Activity.objects.filter(banner=obj).count(), obj.limits)
	showed.short_description = 'Показы'

	def clicked(obj):
		clicks = Activity.objects.filter(banner=obj,clicked=True).count()
		shows = Activity.objects.filter(banner=obj).count()
		return '%s / %s' % (clicks, shows)
	clicked.short_description = 'Клики'

	def ctr(obj):
		clicks = Activity.objects.filter(banner=obj,clicked=True).count()
		shows = Activity.objects.filter(banner=obj).count()
		if shows == 0:
			shows = 1
		ctr = float(clicks) / shows * 100
		return '%s %%' % (ctr)
	ctr.short_description = 'CTR'

	def __unicode__(self):
		return u'#%s %s' % (self.id, self.name)

	class Meta:
	    verbose_name = "Баннер"
	    verbose_name_plural = "Баннеры"

class UserBase(models.Model):
	last_visit = models.DateTimeField(verbose_name='Дата последнего визита')
	ip = models.CharField(max_length=255, verbose_name='IP-адрес посетителя')
	gender_male = models.BooleanField()
	cookie = models.CharField(max_length=255, unique=True, verbose_name='Cookie')
	from_user = models.CharField(max_length=255, verbose_name='Откуда пришол пользователь')
	def __str__(self):
		return u'Пользователь %s' % (self.cookie)
	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

class Activity(models.Model):
	banner = models.ForeignKey(Banner, verbose_name='Баннер')
	date_of_show = models.DateTimeField(verbose_name='Дата показа баннера')
	clicked = models.BooleanField(verbose_name='Было ли совершено нажатие?')
	url_hash = models.CharField(max_length=255, verbose_name='HASH для формирования ссылки')
	user = models.ForeignKey(UserBase, verbose_name='Пользователь')
	class Meta:
		verbose_name = "Активность: показ и клик"
		verbose_name_plural = "Активность: показы и клики"

class Advertising(models.Model):
	name = models.CharField(verbose_name='Название', max_length=255)
	banner = models.ManyToManyField(Banner, verbose_name='Банер')
	class Meta:
		verbose_name = "Рекламая кампания"
		verbose_name_plural = "Рекламные кампании"

class Tages(models.Model):
	name = models.CharField(verbose_name='Имя тега', max_length=255)
	desc = models.CharField(verbose_name='Описание тега', max_length=255)
	#ali_key = models.
	class Meta:
		verbose_name = "Тег"
		verbose_name_plural = "Теги"

class RubricTag(models.Model):
	name = models.CharField(verbose_name='Название', max_length=255)
	desc = models.CharField(verbose_name='Описание тега', max_length=255)
	#ali_key = models.
	class Meta:
		verbose_name = "Рубрика тега"
		verbose_name_plural = "Рубрики тегов"
			
