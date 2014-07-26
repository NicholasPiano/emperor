#blog.urls

#django
from django.conf.urls import patterns, include, url

#local
from blog.views import *

#patterns
urlpatterns = patterns('',
    #frontend-misc
    url(r'^$', IndexView.as_view()),

    #backend
    url(r'^login/$', LoginView.as_view()),

    #blog
    url(r'^blog/', include([
        url(r'^$', OverView.as_view()),
        url(r'(?P<emperor>[a-zA-Z]+)/', include([
            url(r'^$', BlogListView.as_view()),
            url(r'new/', 'blog.views.new_blog'),
            url(r'(?P<blog_id>[a-zA-Z0-9]+)/', include([
                url(r'^$', BlogView.as_view()),
                url(r'new/', 'blog.views.new_post'),
                url(r'(?P<year>[0-9]{4})/', include([
                    url(r'^$', YearArchiveView.as_view()),
                    url(r'(?P<month>[0-9]{2})/', include([
                        url(r'^$', MonthArchiveView.as_view()),
                        url(r'(?P<day>[0-9]{2})/(?P<index>[0-9]+)/$', PostView.as_view()),
                    ])),
                ])),
            ])),
        ])),
    ])),
)
