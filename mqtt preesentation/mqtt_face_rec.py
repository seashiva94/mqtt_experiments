
from picamera.array import PiRGBArray
from picamera import PiCamera
import paho.mqtt.client as mqtt
import time
import cv2

def on_connect(client, user_data, flags, rc):
	if rc == 0:
		print "connected to mqtt server"
	else:
		print "error connecting to broker"

def on_log(client, user_data, buff):
	print "log : ", buff

client = mqtt.Client('face_rec')
client.on_connect = on_connect

client.connect('10.0.0.8')
client.loop_start()

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 10 # set frame rate
raw_capture = PiRGBArray(camera, size=(640,480)) #store camera image in memory

time.sleep(1) # let  camera warmup

face_cascade = cv2.CascadeClassifier('faces.xml')

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
	image = raw_capture.array
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	print "found :", len(faces), "faces"
	client.publish("topic/faces", str(len(faces)))
	raw_capture.truncate(0) # clears the stream for next frame

