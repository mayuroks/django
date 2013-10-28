from django.conf.urls import patterns, include, url
import blog.views
from blog.api import ColinResource

colin_resource = ColinResource()


urlpatterns = patterns('',
    url(r'^api/', include(colin_resource.urls)),
    url(r'^$', blog.views.BlogListView.as_view(), name='home'),
    url(r'^newpost$', blog.views.CreateFormView.as_view(), name='post-form'),
    # url(r'post-update/(?P<slug>[-\w]+)/$', blog.views.UpdateFormView.as_view(), name="update-form"),
    url(r'post-update/(?P<slug>[-\w]+)/$', blog.views.UpdateFormView.as_view(), name="update-form"),
	url(r'post-delete/(?P<slug>[-\w]+)/$', blog.views.PostDeleteView.as_view(), name="post-delete"),
    ## VIDEO URLS
    url(r'^vids$', blog.views.VidList.as_view(), name="vlist"),
    url(r'^vids-upload$', blog.views.VidUpload.as_view(), name="vupload"),
    url(r'^vids-details/(?P<pk>\d+)/$', blog.views.VidDetails.as_view(), name="vdetails"),
    # url(r'^microblog/', include('microblog.foo.urls')),

    url(r"^blog/(?P<pk>\d+)/$", blog.views.PostDetailView.as_view(), name="post-details"),
)