"""URL patterns for the website."""

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from screencasts.feeds import LatestScreencasts

admin.autodiscover()


urlpatterns = patterns('screencasts.views',
    url(r'^$', 'home'),
    url(r'^about/$', 'about'),
    url(r'^code/$', 'code'),
    url(r'^donate/$', 'donate'),
    url(r'^screencast/(?P<slug>[-\w]+)/$', 'screencast'),
    url(r'^feed/$', LatestScreencasts()),
)


urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
