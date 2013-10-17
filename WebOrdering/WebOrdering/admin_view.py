from django.http import HttpResponse
from django.template import Template,Context

def admin(request):
    text=open('WebOrdering/admin_login.html').read()
    return HttpResponse(text)
