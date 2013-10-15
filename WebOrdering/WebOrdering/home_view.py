from django.http import HttpResponse

def home(request):
    text=open('WebOrdering/home.html').read()
    return HttpResponse(text)