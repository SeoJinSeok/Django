from django.conf.urls import patterns, include, url
from a.api import EntryResource

entry_resource = EntryResource()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^test2/', include('a.urls')),
    (r'^api/', include(entry_resource.urls)),
                    
    # Examples:
    # url(r'^$', 'test2.views.home', name='home'),
    # url(r'^test2/', include('test2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
