from tastypie.resources import ModelResource
from blog.models import Entries

class EntriesResource(ModelResource):
  class Meta:
      queryset = Entries.objects.all()
      resource_name = 'entries'
