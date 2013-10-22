from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context
import sqlite3


def old_customer(request):
    if request.GET.has_key('phone'):
        phone = request.GET['phone']
        text = open('WebOrdering/old_customer.html').read()
        return HttpResponse(Template(text).render(Context({'phone':phone})))
    text=open('WebOrdering/old_customer.html').read()
    return HttpResponse(text)

def new_customer(request):
    if request.GET.has_key('phone'):
        phone = request.GET['phone']
        text = open('WebOrdering/new_customer.html').read()
        return HttpResponse(Template(text).render(Context({'phone':phone})))
    text=open('WebOrdering/new_customer.html').read()
    return HttpResponse(text)

def check_phone(request):
    if request.POST.has_key('mobi'):
        phone=request.POST['mobi']
        if is_old_customer(phone):
            return HttpResponse('/old_customer')
        else:
            return HttpResponseRedirect('/new_customer?phone='+phone)
    text=open('WebOrdering/check_phone.html').read()
    return HttpResponse(text)

def submit(request):
    text=open('WebOrdering/submit.html').read()
    if request.GET.has_key('food_list'):
        food_list=request.GET['food_list']
        food_list=food_list.split(',')
        return HttpResponse(Template(text).render(Context({'orders':get_order_list(food_list)})))
    return HttpResponse(Template(text).render(Context(None)))

def check_submit(request):
    user_dict={'name':'test','address':'16#313','phone':'12345678901','totalprice':50}
    text=open('WebOrdering/check_submit.html').read()
    return HttpResponse(Template(text).render(Context(user_dict)))

def choose_food(request):
    text=open('WebOrdering/choose_food.html').read()
    return HttpResponse(text)

def is_old_customer(phone):
    db = sqlite3.connect('WebOrdering/user.db')
    cur = db.cursor()
    cur.execute("select * from user where telephone='%s'" % phone)
    data = cur.fetchone()
    db.close()
    return data

def get_order_list(food_list):
    db=sqlite3.connect('WebOrdering/menu.db')
    cur=db.cursor()
    for item in food_list:
        rs=cur.execute("select * from menu where foodname='%s'" % item)
        yield rs.fetchone()
    db.close()