import MySQLdb
db = MySQLdb.connect("localhost","root","huynam","wsn")
cursor = db.cursor()
cursor = db.cursor()
sql = "delete from sensors where id<2"
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()
