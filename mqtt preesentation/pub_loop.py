import paho.mqtt.client as mqtt
import time
import random

def on_connect(client, user_data, flags, rc):
	if rc==0:
		print "connected OK"
	else:
		print "error connecting to server"

def on_log(client, userdata, level, buff):
	print "log : ", buff

def on_disconnect(client, user_data, flags, rc=0):
	print "disconnected with code :", rc


def frown(client, topic):
	print "frown"
	message = "ON OFF OFF OFF OFF ON"
	m1 = " ".join(message.split(" ")[0:4])
	m2 = " ".join(message.split(" ")[4:])
	client.publish(topic, m1)
	client.publish(topic+"2", m2)
	time.sleep(2.5)
	off(client, topic)

def smile(client, topic):
	print "smile"
	message = "OFF ON ON ON ON OFF"
	m1 = " ".join(message.split(" ")[0:4])
	m2 = " ".join(message.split(" ")[4:])
	client.publish(topic, m1)
	client.publish(topic+"2", m2)
	time.sleep(2.5)
	off(client, topic)

def off(client, topic):
	print "off"
	message = "OFF OFF OFF OFF"
	client.publish(topic, message)
	client.publish(topic+"2", message)


def on(client, topic):
	print "ON"
	message = "ON ON ON ON"
	client.publish(topic, message)
	client.publish(topic+"2", message)
	time.sleep(3)
	off(client, topic)

def wave3(client, topic):
	print "WAVE"
	message = [ "" for  i in range(8)]

	message[0] = "ON OFF OFF OFF"
	message[1] = "ON ON OFF OFF"
	message[2] = "ON ON ON OFF"
	message[3] = "ON ON ON ON"

	message[4] = "OFF ON ON ON"
	message[5] = "OFF OFF ON ON"
	message[6] = "OFF OFF OFF ON"
	message[7] = "OFF OFF OFF OFF"
	for i in range(8):
		client.publish(topic, message[i])
		time.sleep(0.75)

def alternate(client, topic):
	print "alternate"
	message = ["ON OFF ON OFF ON OFF", "OFF ON OFF ON OFF ON"]
	for m in message:
		m1 = " ".join(m.split(" ")[0:4])
		m2 = " ".join(m.split(" ")[4:])
		client.publish(topic,m1)
		client.publish(topic+"2",m2)
		time.sleep(2.5)

#broker = "iot.eclipse.org"
#broker = "10.0.0.8"
broker = "127.0.0.1"

client = mqtt.Client("doby's ppublisher")
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
print "connecting to broker"

##async loop rins in a separate thread, for callbacks to be processed
client.connect(broker)
client.loop_start()

while True:
	#""""
	print "smile and recover "
	smile(client, "topic/dendrite/respond")
	print "sleeping"
	time.sleep(20)
	print "frown and recover"
	frown(client, "topic/dendrite/respond")
	print "sleeping"
	time.sleep(20)

	print "all on and recover"
	on(client, "topic/dendrite/respond")
	time.sleep(20)

	print "alternate"
	alternate(client, "topic/dendrite/respond")
	time.sleep(20)

#print "WAVE 3"
#wave3(client, "topic/dendrite/respond")
"""
msg_list = ["ON", "OFF"]
while True:
	message = ""
	for i in range(4):
		message += " "+random.choice(msg_list)

	client.publish("topic/dendrite/respond", message)
	time.sleep(2)
"""

client.loop_stop()
client.disconnect()
