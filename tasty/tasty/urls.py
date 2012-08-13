from django.conf.urls import patterns, include, url
from tastypie.api import Api
from blog.api import EntryResource, UserResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

urlpatterns = patterns('',
    # The normal jazz here...
    (r'^api/', include(v1_api.urls)),
    # Examples:
    # url(r'^$', 'tasty.views.home', name='home'),
    # url(r'^tasty/', include('tasty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
