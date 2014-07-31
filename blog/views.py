#django
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect

#local
from blog.models import Blog, Emperor

#util


### FRONTEND ###
class IndexView(View): #index.html
    def get(self, request):
        blogs = Blog.objects.all()
        emperors = Emperor.objects.all()

        return render(request, 'blog/index.html', {'blogs':blogs,'emperors':emperors})

class OverView(View): #overview.html
    def get(self, request):
        return render(request, 'blog/overview.html', {'content':'Blog list'})

class SignupView(View):
    def get(self, request):
        return HttpResponse('Sign up')

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

def new_post(request, emperor=None, blog_id=None, **kwargs): #redirects to EditorView, kwargs for link from post
    pass

def delete_post(request, emperor=None, blog_id=None, year=None, month=None, day=None, index=None): #redirects to BlogView
    pass
