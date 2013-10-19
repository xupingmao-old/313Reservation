import sqlite3

conn = sqlite3.connect('user.db')
curs = conn.cursor()
curs.execute(''' CREATE TABLE user(
  id     INTEGER PRIMARY KEY,
  telephone  varchar(11),
  username   varchar(20),
  address    varchar(50),
  sex        varchar(2)
  )
''')
query='INSERT INTO user VALUES (?,?,?,?,?)'

conn = sqlite3.connect('menu.db')
curs = conn.cursor()
curs.execute('''
CREATE TABLE menu(
  foodid     INTEGER PRIMARY KEY,
  foodname   varchar(20),
  foodimage  varchar(50),
  foodprice  FLOAT,
  category   varchar(20),
  introduce  TEXT
  )
''')
query='INSERT INTO menu VALUES (?,?,?,?,?,?)'


conn = sqlite3.connect('order.db')
curs = conn.cursor()
curs.execute('''
CREATE TABLE [order](
  orderid    INTEGER PRIMARY KEY,
  userid     INTEGER,
  foodid     INTEGER,
  amount     INTEGER,
  totalprice FLOAT
  )
''')
query='INSERT INTO [order] VALUES (?,?,?,?,?)'

conn = sqlite3.connect('admin.db')
curs = conn.cursor()
curs.execute('''
CREATE TABLE admin(
  id    INTEGER PRIMARY KEY,
  account    varchar(50),
  password   varchar(50)
  )
''')
conn.close()

print 'table struct in user.db'
conn=sqlite3.connect('user.db')
for i in conn.iterdump():print i

print '\ntable struct in menu.db'
conn=sqlite3.connect('menu.db')
for i in conn.iterdump():print i

print '\ntable struct in order.db'
conn=sqlite3.connect('order.db')
for i in conn.iterdump():print i

print '\ntable struct in admin.db'
conn=sqlite3.connect('admin.db')
for i in conn.iterdump():print i

conn.close()
print 'done!,please enter any key to quit'
raw_input()
