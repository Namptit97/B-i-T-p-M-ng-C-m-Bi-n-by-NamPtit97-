import pymysql
db = pymysql.connect("localhost","root","huynam","wsn")
cursor = db.cursor()
sql = "delete from sensors where id<2"
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()
