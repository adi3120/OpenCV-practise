import cv2 as cv
import numpy as np
import os

face_cascade=cv.CascadeClassifier('har_face.xml')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

cap=cv.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)


people=[]

for i in os.listdir(r'E:\pythons\images\train'):
	people.append(i)


while True:
	_,img=cap.read()
	imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

	faces_rect=face_cascade.detectMultiScale(imgGray,1.1,4)

	for (x,y,w,h) in faces_rect:
		faces_roi=imgGray[y:y+h,x:x+w]
		label,confidence=face_recognizer.predict(faces_roi)

		print("confident = ",confidence)
		print("Name = ",people[label])

		cv.putText(img,people[label],(x,y+h+50),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,0),thickness=2)
		cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

	cv.imshow('Person',img)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break
cv.release()
cv.destroyAllWindows()




	
	
