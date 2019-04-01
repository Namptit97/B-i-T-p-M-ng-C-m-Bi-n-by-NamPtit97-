import MySQLdb
db = MySQLdb.connect("localhost","root","huynam","wsn")
cursor = db.cursor()
# tao 1 bang
sql = "select * from sensors"
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	print results
except:
	print "Khong co du lieu"
db.close()
