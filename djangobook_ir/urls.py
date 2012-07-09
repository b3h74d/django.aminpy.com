from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', views.index),
    (r'^', include("contactus.urls")),
    (r'^djangobook/$', views.toc),
    (r'^aboutdjangobook/$', views.about_book),
    (r'^djangobook(?P<number>\d\d)/$', views.controller),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
