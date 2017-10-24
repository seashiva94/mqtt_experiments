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
	values = s.split(" ")
	print  values

broker = "iot.eclipse.org"

client = mqtt.Client("doby's ssubscriber")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message
print "connecting to broker"

##async loop rins in a separate thread, for callbacks to be processed
client.connect(broker)
client.subscribe("topic/hierarchy/like")

while True:
	#time.sleep(0.001)
	client.loop_start()

client.loop_stop()
client.disconnect()
