from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context
import sqlite3


def old_customer(request):
    text=open('WebOrdering/old_customer.html').read()
    return HttpResponse(text)

def new_customer(request):
    text=open('WebOrdering/new_customer.html').read()
    return HttpResponse(text)

def check_phone(request):
    if request.POST.has_key('mobi'):
        name=request.POST['mobi']
        if is_old_customer(name):
            return HttpResponseRedirect('/old_customer')
        else:
            return HttpResponseRedirect('/new_customer')
    text=open('WebOrdering/check_phone.html').read()
    return HttpResponse(text)

def submit(request):
    text=open('WebOrdering/submit.html').read()
    return HttpResponse(text)

def check_submit(request):
    user_dict={'name':'test','address':'16#313','phone':'12345678901','totalprice':50}
    text=open('WebOrdering/check_submit.html').read()
    return HttpResponse(Template(text).render(Context(user_dict)))

def choose_food(request):
    text=open('WebOrdering/choose_food.html').read()
    return HttpResponse(text)

def is_old_customer(name):
    return False