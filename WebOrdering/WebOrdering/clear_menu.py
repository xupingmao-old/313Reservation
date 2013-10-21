import sqlite3

db=sqlite3.connect('menu.db')
db.execute('delete from [menu]')
db.commit()
db.close()
