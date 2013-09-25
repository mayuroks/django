# Import your generic views here.
from django.views.generic import ListView
from django.views.generic import DetailView

# Import your Tables/ Models
from blog.models import Post

# Make your view classes
class BlogListView(ListView):
	model = Post
	template_name = "index.html"	# Magic happens here

class PostDetailView(DetailView):
	model = Post
	template_name = "details.html"	# need to understand more about context