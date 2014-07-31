#blog.urls

#django
from django.conf.urls import patterns, include, url

#local
from blog.views import *

#patterns
urlpatterns = patterns('',
    #frontend-misc
    url(r'^$', IndexView.as_view()),
    url(r'emperors/', EmperorListView.as_view()),
    url(r'signup/', SignupView.as_view()),

    #backend
    url(r'^login/$', LoginView.as_view()),
    url(r'^empire/$', EmpireView.as_view()),

    #blog
    url(r'^blog/', include([
        #landing
        url(r'^$', OverView.as_view()),
        #emperor is specified
        url(r'(?P<emperor>[a-zA-Z]+)/', include([
            #go to emperor's list of blogs
            url(r'^$', BlogListView.as_view()), #vars: emperor
            #new blog?
            url(r'new/', 'blog.views.new_blog'), #vars: emperor
            #blog id is specified
            url(r'(?P<blog_id>[a-zA-Z0-9]+)/', include([
                #go to blog archive
                url(r'^$', BlogView.as_view()), #vars: emperor, blog_id
                #delete blog?
                url(r'delete/', 'blog.views.delete_blog'), #vars: emperor, blog_id
                #new post?
                url(r'new/', 'blog.views.new_post'), #vars: emperor, blog_id
                #narrowing archive to year
                url(r'(?P<year>[0-9]{4})/', include([
                    url(r'^$', YearArchiveView.as_view()), #vars: emperor, blog_id, year
                    url(r'(?P<month>[0-9]{2})/', include([
                        url(r'^$', MonthArchiveView.as_view()), #vars: emperor, blog_id, year, month
                        #index because there might be more than one post on a day
                        url(r'(?P<day>[0-9]{2})/(?P<index>[0-9]+)/$', include([
                            url(r'^$', PostView.as_view()), #vars: emperor, blog_id, year, month, day, index
                            url(r'edit/', EditorView.as_view()), #vars: emperor, blog_id, year, month, day, index
                            url(r'new/', 'blog.views.new_post'), #vars: emperor, blog_id
                            url(r'delete/', 'blog.views.delete_post'), #vars: emperor, blog_id, year, month, day, index
                        ])),
                    ])),
                ])),
            ])),
        ])),
    ])),
)
