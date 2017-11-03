import paho.mqtt.client as mqtt
import time

def on_connect(client, user_data, flags, rc):
	if rc==0:
		print "connected OK"
	else:
		print "error connecting to server"

def on_log(client, userdata, level, buff):
	print "log : ", buff

def on_disconnect(client, user_data, flags, rc=0):
	print "disconnected with code :", rc

def on_message(client, userdata, msg):
	s = str(msg.payload)
	print "message recvd :", s
	values = s.strip().split(" ")
	numbers = [0 if s == "OFF" else 1 for s in values]
	print  values, numbers

#broker = "iot.eclipse.org"
broker = "127.0.0.1"

client = mqtt.Client("doby's ssubscriber 2")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message
print "connecting to broker"

##async loop rins in a separate thread, for callbacks to be processed
client.connect(broker)
client.subscribe("topic/hierarchy/like2")

client.loop_forever()
#client.loop_stop()
#client.disconnect()
