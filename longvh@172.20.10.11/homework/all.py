def tao_bang():
	#them thu vien
	import pymysql
	
	#mo ket noi den mysql
	db = pymysql.connect("localhost","root","huynam","wsn")

	#su dung mot doi tuong cursor de truy cap
	cursor = db.cursor()

	#Xoa table neu table da ton tai
	cursor.execute("DROP TABLE IF EXISTS sensors")

	#tao 1 bang
	sql = """create table sensors(
		        id int(10) primary key auto_increment,
		        temperature int(3) not null,
		        humidity int(3) not null,
		        time datetime not null ) """

	#thuc thi
	cursor.execute(sql)

	#dong ket noi
	db.close()

def them_dulieu():
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

def sua_dulieu():
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

def xoa_dulieu():
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

def truy_van_dulieu():
	import pymysql
	db = pymysql.connect("localhost","root","huynam","wsn")
	cursor = db.cursor()
	# thuc hien truy van thong tin trong table
	sql = "select * from sensors"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print (results)
	except:
		print ("Khong co du lieu")
	db.close()
