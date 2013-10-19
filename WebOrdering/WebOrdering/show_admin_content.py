import sqlite3

db=sqlite3.connect('admin.db')
cur=db.cursor()

for raw in cur.execute('select * from admin'):
    print raw

db.close()

raw_input()