from django.contrib import admin
from blog.models import Entry

class EntryAdmin (admin.ModelAdmin):
    list_display = ( 'user', 'title', 'body',)
admin.site.register(Entry, EntryAdmin)
