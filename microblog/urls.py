from django.conf.urls import patterns, include, url
import blog.views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', blog.views.BlogListView.as_view(), name='home'),
    url(r'^newpost$', blog.views.CreateFormView.as_view(), name='post-form'),
    url(r'post-update/(?P<slug>[-\w]+)/$', blog.views.UpdateFormView.as_view(), name="update-form"),
	
    ## VIDEO URLS
    url(r'^vids$', blog.views.VidList.as_view(), name="vlist"),
    url(r'^vids-upload$', blog.views.VidUpload.as_view(), name="vupload"),
    url(r'^vids-details/(?P<pk>\d+)/$', blog.views.VidDetails.as_view(), name="vdetails"),
    # url(r'^microblog/', include('microblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r"^blog/(?P<pk>\d+)/$", blog.views.PostDetailView.as_view(), name="post-details"),
)
