# Import your generic views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#from blog.forms import FormPost, UpdatePost
from blog import forms

# Import your Tables/ Models
from blog.models import Post, Colin

# Make your view classes
class BlogListView(ListView):
	model = Post
	template_name = "index.html"	# Magic happens here
	# context_object_name = "mayrok"
	def get_context_data(self, **kwargs):
		context = super(BlogListView, self).get_context_data(**kwargs)
		context['mayrok'] = Post.objects.all()
		return context

class PostDetailView(DetailView):
	model = Post
	template_name = "details.html"	# need to understand more about context

# FORM views
class CreateFormView(CreateView):
	model = Post
	template_name = "create_post_form.html"
	form_class = forms.FormPost
	success_url = "/"

# updating using forms
class UpdateFormView(UpdateView):
	model = Post
	template_name = "create_post_form.html"
	form_class = forms.UpdatePost
	success_url = "/"

	def get_object(self, queryset=None):
		return Post.objects.get(slug=self.kwargs['slug'])

class PostDeleteView(DeleteView):
	model = Post
	template_name = "post_delete.html"
	success_url = "/"

	def get_object(self, queryset=None):
		return Post.objects.get(slug=self.kwargs['slug'])
		
## VIDEOS
class VidList(ListView):
	model = Colin
	template_name = "vid_index.html"
	## URL vids
	context_object_name = "vid_list"

class VidDetails(DetailView):
	model = Colin
	template_name = "video_details.html"
	## URL vids-details
	context_object_name = "vid"	

	def get_context_data(self, **kwargs):
		context = super(VidDetails, self).get_context_data(**kwargs)
		context['vid_list'] = Colin.objects.filter(id__lt=10)
		return context
		
class VidUpload(CreateView):
	model = Colin
	form_class = forms.VidPost
	template_name = "create_post_form.html"
	## URL vids-upload
	success_url = "/vids"








