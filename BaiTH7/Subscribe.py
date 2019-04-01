import paho.mqtt.client as mqtt
from Get_Data_to_DB import *
from time import sleep

# MQTT Settings
MQTT_Broker = "localhost"
MQTT_Port = 1883
Kepp_Alive_Interval = 45
MQTT_Topic_1 = "home/sensors_1"
MQTT_Topic_2 = "home/sensors_2"
MQTT_Topic_3 = "home/sensors_3"
# gui thong bao khi ket noi thanh cong den server
def on_connect(client, userdata, flags, rc):
	if rc != 0: #ket noi thanh cong khi rc = 0
		pass
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))
	client.subscribe(MQTT_Topic_1,0)
#	sleep(3)
	client.subscribe(MQTT_Topic_2,0)
#	sleep(3)
	client.subscribe(MQTT_Topic_3,0)
#gui thong bao khi nhan du lieu duoc publish den topic

def on_message(client, userdata, msg):
	print("MQTT Data Received...")
	print("MQTT Topic: " + msg.topic)
	print("Data: " + str(msg.payload))
	Sensor(msg.payload)
	#try:
    #	Sensor(msg.payload)
	#except:
    #	print("Error")

client = mqtt.Client()
client.username_pw_set(username="huynam",password="huynam")
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_Broker,MQTT_Port,Kepp_Alive_Interval)
client.loop_forever()

