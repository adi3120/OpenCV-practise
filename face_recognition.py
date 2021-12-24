import numpy as np
import cv2 as cv
import os

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

features=np.load('features.npy',allow_pickle=True)
labels=np.load('labels.npy')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

people=[]
for i in os.listdir(r'E:\pythons\images\train'):
	people.append(i)

img=cv.imread(r'E:\pythons\images\train\test7.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('person',gray)

faces_rect=face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
	faces_roi=gray[y:y+h,x:x+w]
	label,confidence=face_recognizer.predict(faces_roi)

	print("confident = ",confidence)
	print("name = ",people[label])

	cv.putText(img,people[label],(x,y+h+50),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),thickness=2)
	cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

cv.imshow('Result',img)	

cv.waitKey(0)


