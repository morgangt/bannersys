# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.template import Context, Template
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from functools import reduce
from django.shortcuts import render
from django.db.models import Q
from django.conf import settings
from django import template 
from operator import or_
from datetime import *
import time
from main.models import Banner, OutputTemplates, Activity, UserBase
import hashlib
import random
import sys
#указываем константу для перехода, в случае не коректной ссылки
VarHome = HttpResponseRedirect(settings.SITE_LINK)
now = datetime.now()

def main(request):
	hi = "<h1>It's main page or index page</h1><br/><a href='test'>testing</a>"
	answer = HttpResponse(hi)
	return answer

@csrf_exempt
def get(request):
	sol = 'sol=))lol'#соль добавляется при составение Хэша
	answer = HttpResponse('nothing')
	if request.method == 'POST':#если нам всетаки прислали запрос на шаблон
		#определяем шаблон
		if request.POST['template'].isdigit():
			t = int(request.POST['template'])
		else:# если не определили то по умалчанию ставим первый (он будет универсальым)
			t = 1
		#определяем тэги которые нам присали
		if request.POST['tags']:
			targtag = request.POST['tags'].split(',')#составляем список, новый элемент списка отделен запятой
			targtag.append("defult")
		else:# если так случилось что тегов нет, стаивм по умалчанию
			targtag = 'defult'
		alltemplate = OutputTemplates.objects.get(id=t)	#извлекаем из бд нужный нам шаблон
		temp = Template(alltemplate.template)#приравниваем к переменной выбранный шаблон 
		##определяемся с местом показа
		if request.POST['place']:
			place = request.POST['place']
		##добавить место по умолчанию, квадратный баннер например 250х250 пикселей

		##--- ip ---#
		if 'u_cookie_banner_system' in request.COOKIES:##Проверяем есть ли cookie у пользователя
			cuid = request.COOKIES.get('u_cookie_banner_system')
			try:
				user = UserBase.objects.get(cookie=cuid)
				user.save()
			##если cookie старый или его почемуто нет в бд тоогда даем user новый cookie
			except ObjectDoesNotExist:
				referer = request.META.get('HTTP_REFERER')
				x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
				if x_forwarded_for:
					ip = x_forwarded_for.split(',')[-1].strip()
				else:
					ip = request.META.get('REMOTE_ADDR')	
				cuk = now.__str__()+ip.__str__()+place
				cukie = hashlib.md5(cuk.encode('utf-8')).hexdigest()
				user = UserBase(last_visit=now, ip=ip, gender_male=False, cookie=cukie, from_user=referer)
				answer.set_cookie('u_cookie_banner_system', cukie)
				user.save()
		else:
			# запишем ip-адрес
			referer = request.META.get('HTTP_REFERER')
			x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
			if x_forwarded_for:
				ip = x_forwarded_for.split(',')[-1].strip()
			else:
				ip = request.META.get('REMOTE_ADDR')	
			cuk = now.__str__()+ip.__str__()+place
			cukie = hashlib.md5(cuk.encode('utf-8')).hexdigest()
			user = UserBase(last_visit=now, ip=ip, gender_male=False, cookie=cukie, from_user=referer)
			answer.set_cookie('u_cookie_banner_system', cukie)
			user.save()
		
		##--- end ip ---##
		nowtime = now.strftime("%H")##переменная хранящая который час
		##достаем все действительные банера по позиции
		all_banner = Banner.objects.filter(date_from__lte=now, date_to__gte=now, date_time_from__lte=nowtime, date_time_to__gte=nowtime, position__id=place, activ=True)
		##формируем дату для показа
		day = []
		weekday = ['128', '2', '4', '8', '16', '32', '64']
		d = int(now.strftime('%w'))
		if d == 0:
			day.append(128)
			day.append(192)
			day.append(254)
		else:
			if d <= 5:
				day.append(weekday[d])
				day.append(62)
				day.append(254)
			else:
				day.append(weekday[d])
				day.append(192)
				day.append(254)
		all_banners = all_banner.filter(reduce(or_, [Q(date_days=dt) for dt in day]))
		##и отбираем по получиным тегам 
		banner = all_banners.filter(reduce(or_, [Q(targeting_tags__contains=c) for c in targtag]))
		ban = []
		for x in banner:
			ban.append(x.limits_to_user)##тут хранятся все лимиты в ввиде списка
		##---- приоритет ----##
		sump = 0
		if banner.count() == 1:
			n = 0
		else:
			lisp = []
			for i in banner:
				sump += i.priority##сумма всех приоритетов
				lisp.append(sump)##список приоритетов
			p = random.randint(0,sump)##рандомное значение от 0 до суммы всех приоритетов
			##определяем наибольшое число 
			for x in lisp:
				if p < x:
					n = lisp.index(x)##определяем порядковое значение найденого числа
					break##тут заканчиваем цикл если нашли число
		##---- end приоритет ----##
		found = banner[n]	##выбираем конкретный банер который будем показывать
		##пощитаем сколько раз мы уже показали баннер 
		if found.limits <= Activity.objects.filter(banner=found).count():
			found.activ=False
		##состовляем ссылку для перехода
		linkclik = now.ctime()+sol+found.id.__str__()
		##записываем показ банера
		show = Activity(banner=found,date_of_show=now,clicked=False,url_hash=hashlib.md5(linkclik.encode('utf-8')).hexdigest(), user=user)
		show.save()
		##готовим данные для шаблона
		con = Context(
			{
				'img': settings.MEDIA_URL+str(found.file_img),
				'width': found.width,
                'height': found.height,	
                'link_to_1': settings.SITE_LINK+'/getme/?i='+hashlib.md5(linkclik.encode('utf-8')).hexdigest()+'&l=1',
                'link_to_2': settings.SITE_LINK+'/getme/?i='+hashlib.md5(linkclik.encode('utf-8')).hexdigest()+'&l=2'
			}
		)
		answer.content = temp.render(con)
		found.save()
	return answer

@csrf_exempt
def getme(request):
	result = None
	if request.method == 'GET':
		if 'i' in request.GET:
			try:
				sh = Activity.objects.filter(url_hash=request.GET['i'])#используем фильтр, если есть несколько одинаковых ссылок чтобы не было косяков
				show = sh[0]#если попалась два банера на одной страници у них одинаковые ссылки чтобы не было косяка
			except:
				return HttpResponseRedirect('http://ya.ru')
			if 'l' in request.GET:
				if request.GET['l'] == '1':
					result = show.banner.link_to_1
				if request.GET['l'] == '2':
					result = show.banner.link_to_2
				if request.GET['l'] == '3':
					result = show.banner.link_to_3
				if request.GET['l'] == '4':
					result = show.banner.link_to_4
			show.clicked=True
			show.save()
		else:
			#если чтото случилось с сылкой. и нет id в виде хэша тогда перенаправляем на главную
			return  VarHome
	return HttpResponseRedirect(result)

@csrf_exempt
def test(request):
    context = {
        'group': 'group',
        'template': 'template',
        'tags': 'tags',
    }
    return HttpResponse(render_to_string('test.html', context))
