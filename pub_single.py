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

broker = "iot.eclipse.org"

client = mqtt.Client("doby's ppublisher")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
print "connecting to broker"

##async loop rins in a separate thread, for callbacks to be processed
client.connect(broker)
client.loop_start()
time.sleep(2)
client.publish("topic/hierarchy/like", "this is a test message")
time.sleep(5)
client.loop_stop()
client.disconnect()
