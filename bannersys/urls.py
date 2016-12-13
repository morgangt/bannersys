from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bannersys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.main'),
    url(r'^get/$', 'main.views.get'),
    url(r'^getme/', 'main.views.getme'),
    url(r'^test/', 'main.views.test'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
