from django.http import HttpResponse
from django.template import Template,Context
import sqlite3

def home(request):
    if request.GET.has_key('page'):
        page=request.GET['page']
        if page=='new_customer':
            text=open('WebOrdering/new_customer.html').read()
            return HttpResponse(text)
    text=open('WebOrdering/home.html').read()
    foods=get_food_list()
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


def about(request):
    text=open('WebOrdering/about.html').read()
    return HttpResponse(text)


def get_food_list():
    db=sqlite3.connect('WebOrdering/menu.db')
    cur=db.cursor()
    for foodid,foodname,foodimage,foodprice,category,introduce in cur.execute('select * from menu'):
        yield (category,foodimage,foodname,foodprice,introduce)
    db.close()