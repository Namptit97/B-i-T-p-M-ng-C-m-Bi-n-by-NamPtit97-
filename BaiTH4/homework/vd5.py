import pymysql
db = pymysql.connect("localhost","root","huynam","wsn")
cursor = db.cursor()
sql = "update sensors set temperature=30, humidity=80 where id=1"
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()
