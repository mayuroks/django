from django import forms
from blog.models import Post
class FormPost(forms.ModelForm):
	class Meta:
		model = Post

class UpdatePost(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('published',)