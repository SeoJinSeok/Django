from django.contrib import admin
from blog.models import Entries,Categories,TagModel

class EntriesAdmin(admin.ModelAdmin):
    list_display = ('id','Title','created',)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('Title',)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('Title',)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Entries, EntriesAdmin)
admin.site.register(TagModel, TagsAdmin)
