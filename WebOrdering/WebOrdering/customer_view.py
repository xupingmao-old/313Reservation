from django.http import HttpResponse,HttpResponseRedirect

def old_customer(request):
    text=open('WebOrdering/old_customer.html').read()
    return HttpResponse(text)

def new_customer(request):
    text=open('WebOrdering/new_customer.html').read()
    return HttpResponse(text)

def check_phone(request):
    text=open('WebOrdering/check_phone.html').read()
    return HttpResponse(text)

def submit(request):
    text=open('WebOrdering/submit.html').read()
    return HttpResponse(text)

def check_submit(request):
    text=open('WebOrdering/check_submit.html').read()
    return HttpResponse(text)

def choose_food(request):
    text=open('WebOrdering/choose_food.html').read()
    return HttpResponse(text)