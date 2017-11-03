import paho.mqtt.client as mqtt
import time

def on_connect(client, user_data, flags, rc):
	client.subscribe("await_event")
	if rc==0:
		print "connected OK"
	else:
		print "error connecting to server"

def on_log(client, userdata, level, buff):
	print "log : ", buff

def on_disconnect(client, user_data, flags, rc=0):
	print "disconnected with code :", rc

def on_message(client, user_data, flags, rc=0):
	print "msg_recvd"
	client.publish("topic/hierarchy/like", "Kya be chutiye")
	client.publish("topic/hierarchy/like2", "Hat bhosadike")


#broker = "iot.eclipse.org"
broker = "127.0.0.1"

client = mqtt.Client("doby's ppublisher")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message
print "connecting to broker"

##async loop rins in a separate thread, for callbacks to be processed
client.connect(broker)
client.loop_forever()
time.sleep(2)
time.sleep(5)
client.loop_stop()
client.disconnect()
