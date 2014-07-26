#emperor.urls

#django
from django.conf.urls import patterns, include, url

#patterns
urlpatterns = patterns('',
    url(r'', include('blog.urls')),
)
