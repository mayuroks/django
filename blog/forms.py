from django import forms
from blog.models import Post
from django.template.defaultfilters import slugify 
class FormPost(forms.ModelForm):
	class Meta:
		model = Post

	def clean(self):
		cleaned_data = super(FormPost, self).clean()
		title = cleaned_data.get('title') + '__from_form'
		cleaned_data['title'] = title

		slug = cleaned_data.get('slug')
		if not slug:
			cleaned_data['slug'] = slugify(title)
		return cleaned_data
##https://docs.djangoproject.com/en/1.5/ref/forms/validation/#form-and-field-validation
class UpdatePost(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('published',)
