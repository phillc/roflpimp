from django.conf.urls.defaults import *
from roflpimp.settings import DEBUG, MEDIA_ROOT, DEV_SERVER
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'roflpimp.apps.aggregator.views.home', name='home'),
    url(r'^update_user/$', 'roflpimp.apps.aggregator.views.update_user', name='update_user'),
    (r'^admin/(.*)', admin.site.root),
)

if DEBUG and DEV_SERVER:
    urlpatterns += patterns ('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    )
