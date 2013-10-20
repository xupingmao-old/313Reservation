# -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context
from django.shortcuts import render_to_response
import sqlite3
import re
import os
import time
import threading

class MySession:
    def __init__(self):
        self._session={}
        self.timeout=10
        self.t=threading.Thread(target=self.check_timeout)
        self.t.start()

    def has(self,name):
        return self._session.has_key(name)

    def add(self,name):
        if self._session.has_key(name):
            return
        self._session.update({name:time.time()})

    def del_timeout(self):
        now_time=time.time()
        temp=[]
        # find all timeout sessions
        for name in self._session:
            if now_time - self._session[name] > self.timeout:
                temp.append(name)
        # del timeout sessions
        for item in temp:
            del self._session[item]

    def check_timeout(self):
        while 1:
            self.del_timeout()
            print self._session
            time.sleep(3)


my_session=MySession()

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
        my_session.add(username)
        print 'my_session:',my_session._session
        return HttpResponseRedirect('/admin/'+username)
    text=Template(text).render(Context({}))
    return HttpResponse(text)

def is_admin(account,md5_password):
    db=sqlite3.connect('WebOrdering/admin.db')
    cur=db.cursor()
    cur.execute("select * from admin where account='%s'" % account)
    record = cur.fetchone()
    db.close()
    if record:
        password=record[2]
        # print password
        return password==md5_password
    else:return False

def admin_manage(request,username):
    if not my_session.has(username):
        text='''
            <h1>连接超时</h1>
            <a href="/login/admin">重新登录</a><br />
            <a href="/">返回主页</a>
            '''
        return HttpResponse(text)
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