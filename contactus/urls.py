from django.conf.urls.defaults import patterns

import views


urlpatterns = patterns('',
    (r'contactus/$', views.contact_us)
)