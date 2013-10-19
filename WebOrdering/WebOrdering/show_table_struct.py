import sqlite3

con=sqlite3.connect('user.db')
print 'table user:'
for i in con.iterdump():print i

con=sqlite3.connect('menu.db')
print '\ntable menu:'
for i in con.iterdump():print i

con=sqlite3.connect('order.db')
print '\ntable order:'
for i in con.iterdump():print i

con=sqlite3.connect('admin.db')
print '\ntable admin:'
for i in con.iterdump():print i
print '\ndone!'
raw_input()
