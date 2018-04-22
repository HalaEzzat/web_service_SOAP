from tastypie.resources import ModelResource
from .models import Students
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization



class StudentsResource(ModelResource):
    class Meta:
        queryset = Students.objects.all()
        # resource_name = 'postss'
        # allowed_methods = ['get']
        # excludes = ['email', 'password', 'is_superuser']
        serializer = Serializer(formats=['xml', 'json'])
        always_return_data = True
        authorization = Authorization()

        def obj_create(self, bundle, **kwargs):
            return super(StudentsResource, self).obj_create(bundle, **kwargs)

