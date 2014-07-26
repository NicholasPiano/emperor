#django
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect

#local

#util


### FRONTEND ###
class IndexView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')

class OverView(View):
    def get(self, request):
        return HttpResponse('Overview')

class BlogListView(View):
    def get(self, request, emperor=None):
        return HttpResponse('Blog list: ' + emperor)

class EmperorListView(View):
    def get(self, request, emperor=None):
        return HttpResponse('Emperor list')

class BlogView(View):
    def get(self, request, emperor=None, blog_id=None):
        return HttpResponse('Blog: ' + blog_id)

class YearArchiveView(View):
    def get(self, request, emperor=None, blog_id=None, year=None):
        return HttpResponse('Year')

class MonthArchiveView(View):
    def get(self, request, emperor=None, blog_id=None, year=None, month=None):
        return HttpResponse('Month')

class PostView(View):
    def get(self, request, emperor=None, blog_id=None, year=None, month=None, day=None, index=None):
        return HttpResponse('Post')

### BACKEND ##
class LoginView(View):
    def get(self, request):
        return HttpResponse('Login')

class EmpireView(View):
    def get(self, request):
        return HttpResponse('Empire')

class EditorView(View):
    def get(self, request):
        return HttpResponse('Editor')

def new_blog(request, emperor=None): #redirects to BlogView
    pass

def new_post(request, emperor=None, blog_id=None): #redirects to EditorView
    pass

def edit_post(request, emperor=None, blog_id=None, year=None, month=None, day=None, index=None): #redirects to EditorView
    pass
