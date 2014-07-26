#django
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse, HttpResponseRedirect

#local

#util


### FRONTEND ###
class IndexView(TemplateView): #index.html
    template_name = 'blog/index.html'

class OverView(TemplateView): #overview.html
    template_name = 'blog/overview.html'

class BlogListView(View): #archive.html
    def get(self, request, emperor=None):
        return HttpResponse('Blog list: ' + emperor)

class EmperorListView(View): #archive.html
    def get(self, request, emperor=None):
        return HttpResponse('Emperor list')

class BlogView(View): #archive.html
    def get(self, request, emperor=None, blog_id=None):
        return HttpResponse('Blog: ' + blog_id)

class YearArchiveView(View): #archive.html
    def get(self, request, emperor=None, blog_id=None, year=None):
        return HttpResponse('Year')

class MonthArchiveView(View): #archive.html
    def get(self, request, emperor=None, blog_id=None, year=None, month=None):
        return HttpResponse('Month')

class PostView(View): #post.html
    def get(self, request, emperor=None, blog_id=None, year=None, month=None, day=None, index=None):
        return HttpResponse('Post')

### BACKEND ##
class LoginView(View): #login.html
    def get(self, request):
        return HttpResponse('Login')

class EmpireView(View): #empire.html
    def get(self, request):
        return HttpResponse('Empire')

class EditorView(View): #editor.html
    def get(self, request, emperor=None, blog_id=None, year=None, month=None, day=None, index=None):
        return HttpResponse('Editor')

def new_blog(request, emperor=None): #redirects to BlogView
    pass

def delete_blog(request, emperor=None, blog_id=None): #redirects to EmpireView
    pass

def new_post(request, emperor=None, blog_id=None): #redirects to EditorView
    pass

def delete_post(request, emperor=None, blog_id=None, year=None, month=None, day=None, index=None): #redirects to BlogView
    pass
