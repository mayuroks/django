from django import forms
from blog.models import Post

class FormPost(forms.ModelForm):
	class Meta:
		model = Post

	def clean(self):
		self.fields['title'] = self.cleaned_data.get('title') + 'CLEAN_WORK'
		return self.cleaned_data

class UpdatePost(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('published',)
