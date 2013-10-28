from django.conf.urls import patterns, include, url
import blog.urls


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^blog-app/', include(blog.urls)),  ## PREFIX = test/ to blog urls
    url(r'^', include(blog.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
