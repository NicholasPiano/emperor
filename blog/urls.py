#blog.urls

#django
from django.conf.urls import patterns, include, url

#local
from blog.urls import *

#patterns
urlpatterns = patterns('',
    url(r'^$', ),
)
