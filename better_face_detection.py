import cv2 as cv

faceCascade=cv.CascadeClassifier('har_face.xml')
img=cv.imread('images/train/test7.jpg')
imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(imgGray,1.1,10)

for (x,y,w,h) in faces:
	cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



cv.imshow('Person',img)

cv.waitKey(0)