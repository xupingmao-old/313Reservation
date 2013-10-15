from django.http import HttpResponse

def home(request):
    fp=open('WebOrdering/home.html')
    text=fp.read()
    fp.close()
    return HttpResponse(text)

def about(request):
    fp=open('WebOrdering/about.html')
    text=fp.read()
    fp.close()
    return HttpResponse(text)