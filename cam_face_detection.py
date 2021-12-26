import cv2 as cv

cap=cv.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)


faceCascade=cv.CascadeClassifier('har_face.xml')

while True:
	success,img=cap.read()

	imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

	faces=faceCascade.detectMultiScale(imgGray,1.1,10)

	for (x,y,w,h) in faces:
		cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	
	cv.imshow("Face",img)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break
cv.release()
cv.destroyAllWindows()