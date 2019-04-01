import paho.mqtt.client as mqtt
from Get_Data_to_DB import *

# MQTT Settings
MQTT_Broker = "localhost"
MQTT_Port = 1883
Kepp_Alive_Interval = 45
MQTT_Topic = "nam/hearrate"
temp = 0;
# gui thong bao khi ket noi thanh cong den server
def on_connect(client, userdata, flags, rc):
	if rc != 0: #ket noi thanh cong khi rc = 0
		pass
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))
	client.subscribe(MQTT_Topic,0)

#gui thong bao khi nhan du lieu duoc publish den topic

def on_message(client, userdata, msg):
	global temp
	print("MQTT Data Received...")
	print("MQTT Topic: " + msg.topic)
	print("Data: " + str(msg.payload))
	Sensor(msg.payload)
#	try:
 #   	Sensor(msg.payload)
#	except:
 #   	print("Error")

client = mqtt.Client()
client.username_pw_set(username="huynam",password="huynam")
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_Broker,MQTT_Port,Kepp_Alive_Interval)
client.loop_forever()

