#Them thu vien
import pymysql

#Mo ket noi den MySQL
db = pymysql.connect("localhost","root","huynam","wsn")


cursor = db.cursor()

#Them du lieu vao mot bang
sql = """insert into sensors(temperature, humidity, time)
	 values(14,24,'2019-02-03 09:30:25')"""

#thuc thi
try: #chay binh thuong va bat loi
     #thuc thi lenh sql
        cursor.execute(sql)
     #Xac nhan du lieu
        db.commit()
except: #neu gap loi
	#tro ve luc dau neu gap loi
        db.rollback()
db.close()


