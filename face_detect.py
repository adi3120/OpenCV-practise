import cv2 as cv
orgImg=cv.imread('images/uhhm.jpeg')

img=cv.resize(orgImg,(2000,800))

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_rect= face_cascade.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 5)

for (x,y,w,h) in faces_rect:
	cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=6)

cv.imshow('faces',img)

print(f'Number of faces found = {len(faces_rect)}')

cv.waitKey(0)