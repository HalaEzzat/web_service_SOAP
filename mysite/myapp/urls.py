from django.conf.urls import url, include
from tastypie.api import Api
from myapp.resources import StudentsResource

v1_api = Api(api_name='v1')

v1_api.register(StudentsResource())

