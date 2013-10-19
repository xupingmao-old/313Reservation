import sqlite3,md5
import time

account=raw_input('accout:')
password=raw_input('password:')
m=md5.new()
m.update(password)
md5_password=m.hexdigest()

db=sqlite3.connect('admin.db')
sql="insert into admin values(%d,'%s','%s')" % (int(time.time()),account,md5_password)
db.execute(sql)
db.commit()
db.close()

print 'done'
raw_input()
