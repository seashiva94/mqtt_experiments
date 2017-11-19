import picamera
import time
import cv2

#camera = picamera.PiCamera()
#time.sleep(0.5)
#camera.capture('image.jpg')

#time.sleep(2)
#image = cv2.imread('leo.jpg')
image = cv2.imread('multiface.jpg')
#image = cv2.imread('image.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('faces.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print "Found "+str(len(faces))+" face(s)"

for (x,y,w,h) in faces:
    cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),2)

#Save the result image
cv2.imwrite('grey.jpg', gray)
