from django.http import HttpResponse

def home(request):
    text=open('WebOrdering/home.html').read()
    return HttpResponse(text)

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