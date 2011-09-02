"""URL patterns for the website."""

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from screencasts.feeds import LatestScreencasts

admin.autodiscover()


urlpatterns = patterns('screencasts.views',
    url(r'^$', 'home'),
    url(r'^page/(?P<page_num>\d+)$', 'home'),
    url(r'^about/$', 'about'),
    url(r'^code/$', 'code'),
    url(r'^screencast/(?P<slug>[-\w]+)/$', 'screencast'),
    url(r'^feed/$', LatestScreencasts()),
)


urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
