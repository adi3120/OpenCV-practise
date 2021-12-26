import cv2 as cv
import numpy as np

path='images/car.jpg'

cv.namedWindow('TrackBars')
cv.resizeWindow('TrackBars',640,240)

def empty(a):
	pass
cv.createTrackbar('Hue Min','TrackBars',0,179,empty)
cv.createTrackbar('Hue Max','TrackBars',12,179,empty)
cv.createTrackbar('Sat Min','TrackBars',34,255,empty)
cv.createTrackbar('Sat Max','TrackBars',255,255,empty)
cv.createTrackbar('Val Min','TrackBars',91,255,empty)
cv.createTrackbar('Val Max','TrackBars',255,255,empty)

while True:
	img=cv.imread(path)
	img=cv.resize(img,(500,500))
	imgHSV=cv.cvtColor(img,cv.COLOR_BGR2HSV)
	h_min=cv.getTrackbarPos('Hue Min','TrackBars')
	h_max=cv.getTrackbarPos('Hue Max','TrackBars')
	s_min=cv.getTrackbarPos('Sat Min','TrackBars')
	s_max=cv.getTrackbarPos('Sat Max','TrackBars')
	v_min=cv.getTrackbarPos('Val Min','TrackBars')
	v_max=cv.getTrackbarPos('Val Max','TrackBars')

	lower=np.array([h_min,s_min,v_min])
	upper=np.array([h_max,s_max,v_max])

	mask=cv.inRange(imgHSV,lower,upper)
	
	cv.imshow('HSV',imgHSV)
	cv.imshow('Original',img)
	cv.imshow('Mask',mask)
	cv.imshow('ColorPicked',imgResult)
	
	cv.waitKey(1)	

cap.release()
cv.destroyAllWindows()


