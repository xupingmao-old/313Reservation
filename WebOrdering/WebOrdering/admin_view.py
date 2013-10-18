from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context
import sqlite3
import re

def admin(request):
    text=open('WebOrdering/admin_login.html').read()
    return HttpResponse(text)

def admin_login(request):
    text=open('WebOrdering/admin_login.html').read()
    username,password='',''
    if 'username' in request.GET:
        username=request.GET['username']
    if 'password' in request.GET:
        password=request.GET['password']
    if is_admin(username,password):
        return HttpResponseRedirect('/admin/'+username)
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
    text=open('WebOrdering/admin_manage.html').read()
    return HttpResponse(Template(text).render(Context({'admin_name':username})))
