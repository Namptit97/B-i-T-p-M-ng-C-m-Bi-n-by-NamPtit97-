import MySQLdb
db = MySQLdb.connect("localhost","root","huynam","sensor")
cursor = db.cursor()
db.close()
