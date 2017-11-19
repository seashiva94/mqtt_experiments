from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 30 # set frame rate
raw_capture = PiRGBArray(camera, size=(640,480)) #store camera image in memory

time.sleep(1) # let  camera warmup

face_cascade = cv2.CascadeClassifier('faces.xml')

for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
	image = raw_capture.array
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	print "found :", len(faces), "faces"

	raw_capture.truncate(0) # clears the stream for next frame
