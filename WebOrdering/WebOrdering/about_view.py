from django.http import HttpResponse

def about(request):
    text=open('WebOrdering/about.html').read()
    return HttpResponse(text)