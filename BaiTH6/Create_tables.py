#Them thu vien
import pymysql

#Mo ket noi den MySQL
db = pymysql.connect("localhost","root","huynam","ktra" )

#Su dung mot doi tuong cursor de truy cap
cursor = db.cursor()

#Xoa table neu table da ton tai
cursor.execute("DROP TABLE IF EXISTS sensors")

#Tao mot bang
sql = """CREATE TABLE sensors(
			id INT(10) PRIMARY KEY AUTO_INCREMENT,
			hearrate int(10) NOT NULL,
			STT char(10) NOT NULL,
#			Humidity INT(3) NOT NULL,  
			Date_and_Time char(30) NOT NULL 
		)
	"""
#Thuc thi
cursor.execute(sql)

#Dong ket noi den MySQL
db.close()