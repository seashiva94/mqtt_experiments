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
	print "message recvd :", str(msg.payload)

broker = "iot.eclipse.org"

client = mqtt.Client("doby's ssubscriber")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message
print "connecting to broker"

##async loop rins in a separate thread, for callbacks to be processed
client.connect(broker)
client.loop_start()
client.subscribe("topic/hierarchy/like")
time.sleep(10)
client.loop_stop()
client.disconnect()
