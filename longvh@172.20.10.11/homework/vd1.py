#them thu vien
import pymysql 

#Mo ket noi den MySQL
db = pymysql.connect("localhost","root","huynam","wsn")

#Su dung mot doi tuong cursor de truy cap
cursor = db.cursor()

#thuc hien truy van SQL bang phuong thuc execute()
cursor.execute("SELECT VERSION()")

#Lay ra mot hang bang phuong thuc fetchone()
data = cursor.fetchone()
print ("Database version: %s " % data)

#dong ket noi den MySQL
db.close()
