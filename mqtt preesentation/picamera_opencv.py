# based on code from https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

#convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imwrite('gray-test.jpg', gray)


#time.sleep(1)

face_cascade = cv2.CascadeClassifier('faces.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

#time.sleep(1)

print "Found "+str(len(faces))+" face(s)"

#Draw a rectangle around every found face
for (x,y,w,h) in faces:
    cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),2)

#Save the result image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imwrite('result.jpg',gray)
