import sqlite3

db=sqlite3.connect('admin.db')
cur=db.cursor()

print 'TABLE ADMIN:'
for raw in cur.execute('select * from admin'):
    print raw

db.close()
print 'Done'

print 'TABLE MENU:'
db=sqlite3.connect('menu.db')
cur=db.cursor()
for raw in cur.execute('select * from menu'):
    print raw

db.close()
print 'Done'

raw_input()
