import MySQLdb
db = MySQLdb.connect("localhost","root","huynam","wsn")
cursor = db.cursor()
#tao mot bang
sql = """insert into sensors(temperature, humidity, time) values(14,24,'2019-02-15 09:55:45')"""
#thuc thi
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()
