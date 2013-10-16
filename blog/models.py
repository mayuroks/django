from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from registration.signals import user_registered
from embed_video.fields import EmbedVideoField
# from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	title = models.CharField(max_length=255,)
	slug = models.SlugField(max_length=255, blank=True, default='')
	content = models.TextField()
	published = models.BooleanField(default=True)

def __unicode__(self):
	return self.title

class ExUserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_human = models.BooleanField()
 
    def __unicode__(self):
        return self.user
	def user_registered_callback(sender, user, request, **kwargs):
		profile = ExUserProfile(user = user)
		profile.is_human = bool(request.POST["is_human"])
		profile.save()

	user_registered.connect(user_registered_callback)

class Colin(models.Model):
	myname = models.CharField(max_length=255,)
	video = EmbedVideoField()