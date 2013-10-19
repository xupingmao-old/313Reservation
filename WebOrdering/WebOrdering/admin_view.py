from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context
from django.shortcuts import render_to_response
import sqlite3
import re
import os
import time


def admin(request):
    text=open('WebOrdering/admin_login.html').read()
    return HttpResponse(text)

def admin_login(request):
    text=open('WebOrdering/admin_login.html').read()
    username,password='',''
    if 'username' in request.POST:
        username=request.POST['username']
    if 'password' in request.POST:
        password=request.POST['password']
    if is_admin(username,password):
        return HttpResponseRedirect('/admin/'+username)
    text=Template(text).render(Context({}))
    return HttpResponse(text)

def is_admin(account,md5_password):
    db=sqlite3.connect('WebOrdering/admin.db')
    cur=db.cursor()
    cur.execute("select * from admin where account='%s'" % account)
    record = cur.fetchone()
    if record:
        password=record[2]
        # print password
        return password==md5_password
    else:return False

def admin_manage(request,username):
    base='WebOrdering/img/'
    if request.FILES.has_key('pic'):
        pic=request.FILES['pic']
        extension=get_extension(pic)
        if extension:
            print pic,'uploaded'
            fname=base+str(time.time())+extension
            fp=open(fname,'wb')
            fp.write(pic.read())
            fp.close()
            return HttpResponseRedirect('/admin/'+username)
    text=open('WebOrdering/admin_manage.html').read()
    return HttpResponse(Template(text).render(Context({'admin_name':username})))


def get_extension(name):
    name=str(name)
    if name.endswith(('.jpg','.JPG')):
        return '.jpg'
    elif name.endswith(('.png','.PNG')):
        return '.png'
    elif name.endswith(('.gif','.GIF')):
        return '.gif'
    else:
        return None

def add_to_db(foodname,foodimage,foodprice,category,introduce):
    db=sqlite3.connect('WebOrdering/menu.db')
    cur=db.cursor()
    cur.execute("insert in menu values(%d,'%s','%s',%f,'%s','%s')",
        int(time.time()),foodname,foodimage,foodprice,category,introduce)
    cur.commit()
    db.close()

def get_food_list():
    db=sqlite3.connect('WebOrdering/menu.db')
    cur=db.cursor()
    for item in cur.execute('select * from menu'):
        yield item