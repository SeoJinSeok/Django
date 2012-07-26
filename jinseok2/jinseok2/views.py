# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def hello(request):
    return HttpResponse("Hello world")

def template_test(request):
    t = get_template('test1.html')
    html = t.render(Context({'message': "추가할 메시지"}))
    return HttpResponse(html)
