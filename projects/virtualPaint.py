import cv2 as cv
import numpy as np


cap=cv.VideoCapture(0)

Cam_width=640
Cam_height=480

cap.set(3,Cam_width)
cap.set(4,Cam_height)

cv.namedWindow('Red TrackBars')
cv.resizeWindow('Red TrackBars',640,480) 

cv.namedWindow('Blue TrackBars')
cv.resizeWindow('Blue TrackBars',640,480) 


myColors=[[84,152,119,255,99,255]]
myColorsValues=[[255,128,0],[0,0,255]]

myPoints_red=[]
myPoints_blue=[]

def empty(a):
	pass

cv.createTrackbar('Hue Min','Red TrackBars',0,179,empty)
cv.createTrackbar('Hue Max','Red TrackBars',10,179,empty)
cv.createTrackbar('Sat Min','Red TrackBars',193,255,empty)
cv.createTrackbar('Sat Max','Red TrackBars',255,255,empty)
cv.createTrackbar('Val Min','Red TrackBars',139,255,empty)
cv.createTrackbar('Val Max','Red TrackBars',255,255,empty)

cv.createTrackbar('Hue Min','Blue TrackBars',84,179,empty)
cv.createTrackbar('Hue Max','Blue TrackBars',152,179,empty)
cv.createTrackbar('Sat Min','Blue TrackBars',119,255,empty)
cv.createTrackbar('Sat Max','Blue TrackBars',255,255,empty)
cv.createTrackbar('Val Min','Blue TrackBars',99,255,empty)
cv.createTrackbar('Val Max','Blue TrackBars',255,255,empty)

def findColor(img):
	imgHSV=cv.cvtColor(img,cv.COLOR_BGR2HSV)
	newPoints_red=[]
	newPoints_blue=[]

	h_min_red=cv.getTrackbarPos('Hue Min','Red TrackBars')
	h_max_red=cv.getTrackbarPos('Hue Max','Red TrackBars')
	s_min_red=cv.getTrackbarPos('Sat Min','Red TrackBars')
	s_max_red=cv.getTrackbarPos('Sat Max','Red TrackBars')
	v_min_red=cv.getTrackbarPos('Val Min','Red TrackBars')
	v_max_red=cv.getTrackbarPos('Val Max','Red TrackBars')

	lower_red=np.array([h_min_red,s_min_red,v_min_red])
	upper_red=np.array([h_max_red,s_max_red,v_max_red])

	mask_red=cv.inRange(imgHSV,lower_red,upper_red)


	h_min_blue=cv.getTrackbarPos('Hue Min','Blue TrackBars')
	h_max_blue=cv.getTrackbarPos('Hue Max','Blue TrackBars')
	s_min_blue=cv.getTrackbarPos('Sat Min','Blue TrackBars')
	s_max_blue=cv.getTrackbarPos('Sat Max','Blue TrackBars')
	v_min_blue=cv.getTrackbarPos('Val Min','Blue TrackBars')
	v_max_blue=cv.getTrackbarPos('Val Max','Blue TrackBars')

	lower_blue=np.array([h_min_blue,s_min_blue,v_min_blue])
	upper_blue=np.array([h_max_blue,s_max_blue,v_max_blue])

	mask_blue=cv.inRange(imgHSV,lower_blue,upper_blue)

	x_red,y_red=getContours(mask_red)
	x_blue,y_blue=getContours(mask_blue)

	cv.circle(imgResult,(x_red,y_red),20,myColorsValues[1],cv.FILLED)
	cv.circle(imgResult,(x_blue,y_blue),20,myColorsValues[0],cv.FILLED)

	if x_red!=0 and y_red !=0:
		newPoints_red.append([x_red,y_red])
	if x_blue!=0 and y_blue !=0:
		newPoints_blue.append([x_blue,y_blue])

	return newPoints_blue,newPoints_red



def getContours(img):
	contours,hierarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
	x,y,w,h=0,0,0,0
	for cont in contours:
		area=cv.contourArea(cont)
		if area>500:
			cv.drawContours(imgResult,cont,-1,(255,0,0),5)
			peri=cv.arcLength(cont,True)
			approx=cv.approxPolyDP(cont,0.02*peri,True)
			x,y,w,h=cv.boundingRect(approx)
	return x+w//2,y


def drawOnCanvas(colorCode):
	
	for point in myPoints_red:
		cv.circle(imgResult,(point[0],point[1]),10,myColorsValues[1],cv.FILLED)
	
	for point in myPoints_blue:
		cv.circle(imgResult,(point[0],point[1]),10,myColorsValues[0],cv.FILLED)

		


while True:
	_, img=cap.read()
	imgResult=img.copy()
	newPoints_blue,newPoints_red=findColor(img)

	if len(newPoints_red)!=0:
		for newP_Red in newPoints_red:
			myPoints_red.append(newP_Red)
	if len(myPoints_red)!=0:
		drawOnCanvas(1)

	if len(newPoints_blue)!=0:
		for newP_Blue in newPoints_blue:
			myPoints_blue.append(newP_Blue)
	if len(myPoints_blue)!=0:
		drawOnCanvas(0)

	

	cv.imshow("Result",imgResult)
	
	if cv.waitKey(1) & 0xFF==ord('d'):
		break	

cap.release()
cv.destroyAllWindows()


