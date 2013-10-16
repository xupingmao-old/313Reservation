from django.http import HttpResponse
from django.template import Template,Context

def home(request):
    text=open('WebOrdering/home.html').read()
    foods=[('img/food1.jpg','apple'),('img/food1.jpg','google'),('img/food1.jpg','microsoft'),]
    return HttpResponse(Template(text).render(Context({'foods':foods})))

def css_resource(request,fname):
    text=open('WebOrdering/'+fname+'.css').read()
    return HttpResponse(text)

def jpg_resource(request,fname):
    text=open('WebOrdering/'+fname+'.jpg','rb').read()
    return HttpResponse(text)

def gif_resource(request,fname):
    text=open('WebOrdering/'+fname+'.gif','rb').read()
    return HttpResponse(text)

def png_resource(request,fname):
    text=open('WebOrdering/'+fname+'.png','rb').read()
    return HttpResponse(text)

def js_resource(request,fname):
    text=open('WebOrdering/'+fname+'.js','rb').read()
    return HttpResponse(text)