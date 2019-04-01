import pymysql
import json

def Sensor(jsonData):
	json_Dict = json.loads(jsonData.decode("utf-8"))
	hearrate = json_Dict['hearrate']
	STT = json_Dict['STT']
#	Humidity = json_Dict['Humidity']
	Date_and_Time = json_Dict['Date_and_Time']
	#Open database connection
	db = pymysql.connect("localhost","root","huynam","ktra")
	cursor = db.cursor()
	sql = """INSERT INTO sensors (hearrate,STT,Date_and_Time) 
			 VALUES (%s,%s,%s)"""
	val = (hearrate,STT,Date_and_Time)
	cursor.execute(sql,val)
	db.commit()
	print("Sensor created new value")
	print("")

	db.close()
