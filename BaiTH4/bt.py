from random import randint
import pymysql
import datetime
db = pymysql.connect("localhost","root","huynam","bt")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS bt_1")
sql = """create table bt_1(
	id int(10) primary key auto_increment,
	sensorid int(3) not null,
	long_a int(3) not null,
	lat int(3) not null,
	temp int(3) not null,
	hum int(3) not null,
	windspeed int(3) not null,
	winddirection varchar(10) not null,
	time datetime not null )"""
cursor.execute(sql)
winddirection =["DONG","TAY","NAM","BAC"]; 
for i in range (0,10):
	a = randint(1,4)
	b = a;
	c = a;
	d = randint(20,30)
	e = randint(80,100)
	f = randint(100,1000)
	z = winddirection[randint(0,3)]
	now = datetime.datetime.now()
	sql="""insert into bt_1(sensorid,long_a,lat,temp,hum,windspeed,winddirection,time)
		values(%d,%d,%d,%d,%d,%d,'%s','%s')""" %(a,b,c,d,e,f,z,now)
	cursor.execute(sql) 
	db.commit() 
cursor.execute("select * from bt_1 order by temp,hum asc")
array = cursor.fetchall();
for i in range(0,3):
	print(array[i][0],array[i][1],array[i][2],array[i][3],array[i][4],array[i][5],array[i][6],array[i][7],array[i][8].strftime("%Y-%m-%d %H:%M:%S"))
db.close()

