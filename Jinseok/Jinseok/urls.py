from django.conf.urls import patterns, include, url
from blog.api import EntriesResource


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

entries_resource = EntriesResource()

urlpatterns = patterns('',
     (r'^api/', include(entries_resource.urls)),
     (r'^blog/$', 'blog.views.index'),
     (r'^blog/page/(?P<page>\d+)/$', 'blog.views.index'),
     (r'^blog/entry/(?P<entry_id>\d+)/$', 'blog.views.read'),
     (r'^blog/write/$', 'blog.views.write_form'),
     (r'^blog/add/post/$', 'blog.views.add_post'),
     (r'^admin/', include(admin.site.urls)),
)
