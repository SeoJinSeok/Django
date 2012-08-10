# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from models import Entries
from django.template import Context, loader

def index(request, page=1):
    page = int(page)
    per_page = 5
    i = per_page
    start_pos = (page - 1) *per_page
    end_pos = start_pos + per_page
    c = Entries.objects.count()
    d = (c/i)+(c%i)
    
    page_title = '블로그 글 목록 화면'

    entries = Entries.objects.all().order_by('-created')[start_pos:end_pos]
    tpl= loader.get_template('list.html')
    ctx=Context({
    'page_title':page_title,
    'entries':entries,
    'current_page':page,
    'page':d,
    })
    return HttpResponse(tpl.render(ctx))    

def read(request, entry_id=None):
    page_title = '블로그 글 읽기 화면'

    current_entry = Entries.objects.get(id=int(entry_id))
    try:
        prev_entry = current_entry.get_previous_by_created()
    except:
        prev_entry = None
    try:
        next_entry = current_entry.get_next_by_created()
    except:
        next_entry = None

    tpl = loader.get_template('read.html')
    ctx = Context({'page_title':page_title,
        'current_entry':current_entry,
        'prev_entry':prev_entry,
        'next_entry':next_entry
    })
    return HttpResponse(tpl.render(ctx))

def write_form(request):
    page_title = '블로그 글 쓰기 화면'
    tpl = loader.get_template('write.html')
    ctx = Context({
        'page_title':page_title
    })
    return HttpResponse(tpl.render(ctx))

def add_post(request):
    entry_title = request.POST['title']
    return HttpResponse('hello %s' % entry_title)
