from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from blog.models import Entry
from tastypie.authentication import BasicAuthentication


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = BasicAuthentication()
        allowed_methods = ['get']
        
class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
