#django
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect

#local

#util


### FRONTEND ###
class BlogListView(View): #index
    def get(self, request):
        return HttpResponse('Hello, World!')

class EmperorListView(View):
    pass

class BlogView(View):
    pass

class YearArchiveView(View):
    pass

class MonthArchiveView(View):
    pass

class PostView(View):
    pass

### BACKEND ##
class LoginView(View):
    pass

class EmpireView(View):
    pass

class EditorView(View):
    pass

def add_blog(request): #redirects to BlogView
    pass

def add_post(request): #redirects to EditorView
    pass
