#blog.urls

#django
from django.conf.urls import patterns, include, url

#local
from blog.views import *

#patterns
urlpatterns = patterns('',
    url(r'^$', BlogListView.as_view()),
)
