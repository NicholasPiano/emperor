#django
from django.views.generic import View

#local

#util


### FRONTEND ###
class BlogListView(View):
    pass

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
