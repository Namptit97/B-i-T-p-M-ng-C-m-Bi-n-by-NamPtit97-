#them thu vien
import MySQLdb
#mo ket noi den mysql
db = MySQLdb.connect("localhost","root","huynam","wsn")
#su dung mot doi tuong cursor de truy cap
cursor = db.cursor()
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
