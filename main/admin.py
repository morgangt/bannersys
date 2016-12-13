from django.contrib import admin
from main.models import Banner, OutputTemplates, Activity, Position, UserBase, Advertising, Tages, RubricTag

# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_from', 'date_to', 'date_days', 'limits', 'targeting_tags', 'ctr', 'showed', 'clicked', 'priority', 'activ')

class OutputTemplatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'template')

class ActivityAdmin(admin.ModelAdmin):
	list_display = ('banner', 'url_hash', 'clicked', 'date_of_show')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'size')

class UserBaseAdmin(admin.ModelAdmin):
	list_display = ('last_visit', 'ip', 'cookie', 'gender_male', 'from_user')

class TagesAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc')	

class RubricTagAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc')

class AdvertisingAdmin(admin.ModelAdmin):
	fields = ['name', 'banner']
		
admin.site.register(RubricTag, RubricTagAdmin)
admin.site.register(Tages, TagesAdmin)
admin.site.register(UserBase, UserBaseAdmin)		
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(OutputTemplates, OutputTemplatesAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Advertising, AdvertisingAdmin)