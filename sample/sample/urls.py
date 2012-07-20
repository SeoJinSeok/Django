from django.conf.urls.defaults import *
from sample.views import hello, template_test

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^test1/$', template_test),)
