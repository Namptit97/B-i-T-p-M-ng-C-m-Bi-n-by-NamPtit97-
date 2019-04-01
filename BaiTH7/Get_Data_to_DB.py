import pymysql
import json

def Sensor(jsonData):
	json_Dict = json.loads(jsonData.decode("utf-8"))
	SensorID = json_Dict['Sensor_ID']
	Temperature = json_Dict['Temperature']
	Humidity = json_Dict['Humidity']
	Date_and_Time = json_Dict['Date']
	#Open database connection
	db = pymysql.connect("localhost","root","huynam","bt7")
	cursor = db.cursor()
	sql = """INSERT INTO sensors (SensorID,Temperature,Humidity,Date_and_Time) 
			 VALUES (%s,%s,%s,%s)"""
	val = (SensorID,Temperature,Humidity,Date_and_Time)
	cursor.execute(sql,val)
	db.commit()
	print("Sensor created new value")
	print("")

	db.close()
