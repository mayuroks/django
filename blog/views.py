# Import your generic views here.
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView

#from blog.forms import FormPost, UpdatePost
from blog import forms

# Import your Tables/ Models
from blog.models import Post

# Make your view classes
class BlogListView(ListView):
	model = Post
	template_name = "index.html"	# Magic happens here

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
		obj = Post.objects.get(id=self.kwargs['id'])
		return obj