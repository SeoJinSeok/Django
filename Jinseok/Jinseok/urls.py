from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^blog/$', 'blog.views.index'),
     (r'^blog/page/(?P<page>\d+)/$', 'blog.views.index'),
     (r'^blog/entry/(?P<entry_id>\d+)/$', 'blog.views.read'),                      
     (r'^admin/', include(admin.site.urls)),
)
