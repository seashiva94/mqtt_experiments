import paho.mqtt.client as mqtt
import time
from cloudmesh.pi import Button
from cloudmesh.pi import GroveRelay
from dendrite_test import Dendrite

dendrites = []

for i in range(2,4):
	d = Dendrite(pin = 2*i, recovery_time = 1, max_on_time=5)
	dendrites.append(d)

#dict = {"ON":1, "OFF":0}

def on_connect(client, user_data, flags, rc):
	client.subscribe("topic/dendrite/respond2")

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
	#relay.on() if s == "ON" else relay.off()

	values = s.strip().split(" ")
	print  values
	for i in range(len(dendrites)):
		if values[i] == "ON":
			dendrites[i].on()
		else:
			dendrites[i].off()

#broker = "iot.eclipse.org"
broker = "10.42.0.1"
#broker = "10.0.1.3"

client = mqtt.Client("doby's ssubscriber")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message
print "connecting to broker"

##async loop rins in a separate thread, for callbacks to be processed
client.connect(broker)
#client.subscribe("topic/dendrite/respond")
#client.loop_start()

print "waiting for button press"
b = Button(pin=2)
listen = 0
while True:
	if True: # b.get() == 1:
		print "button_pressed"
		listen = 1
		client.publish("await_event", "start")
		break

#while True:
client.loop_forever()
client.loop_stop()
client.disconnect()
