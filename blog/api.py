from tastypie.resources import ModelResource
from blog.models import Colin
from tastypie.authorization import Authorization

class ColinResource(ModelResource):
	class Meta:
		queryset = Colin.objects.all()
		resource_name = 'colin'
		authorization= Authorization()