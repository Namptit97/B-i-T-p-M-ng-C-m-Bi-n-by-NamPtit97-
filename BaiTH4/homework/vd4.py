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

