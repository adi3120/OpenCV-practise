import cv2 as cv
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


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

while True:
	_, img=cap.read()

	imgHSV=cv.cvtColor(img,cv.COLOR_BGR2HSV)

	h_min_red=cv.getTrackbarPos('Hue Min','Red TrackBars')
	h_max_red=cv.getTrackbarPos('Hue Max','Red TrackBars')
	s_min_red=cv.getTrackbarPos('Sat Min','Red TrackBars')
	s_max_red=cv.getTrackbarPos('Sat Max','Red TrackBars')
	v_min_red=cv.getTrackbarPos('Val Min','Red TrackBars')
	v_max_red=cv.getTrackbarPos('Val Max','Red TrackBars')

	lower_red=np.array([h_min_red,s_min_red,v_min_red])
	upper_red=np.array([h_max_red,s_max_red,v_max_red])

	mask_red=cv.inRange(imgHSV,lower_red,upper_red)
	imgResult_red=cv.bitwise_and(img,img,mask=mask_red)


	h_min_blue=cv.getTrackbarPos('Hue Min','Blue TrackBars')
	h_max_blue=cv.getTrackbarPos('Hue Max','Blue TrackBars')
	s_min_blue=cv.getTrackbarPos('Sat Min','Blue TrackBars')
	s_max_blue=cv.getTrackbarPos('Sat Max','Blue TrackBars')
	v_min_blue=cv.getTrackbarPos('Val Min','Blue TrackBars')
	v_max_blue=cv.getTrackbarPos('Val Max','Blue TrackBars')

	lower_blue=np.array([h_min_blue,s_min_blue,v_min_blue])
	upper_blue=np.array([h_max_blue,s_max_blue,v_max_blue])

	mask_blue=cv.inRange(imgHSV,lower_blue,upper_blue)

	imgResult_blue=cv.bitwise_and(img,img,mask=mask_blue)
	imgResult_red=cv.bitwise_and(img,img,mask=mask_red)
	
	stacked=stackImages(0.6,([img,imgResult_red,imgResult_blue]))

	cv.imshow('Horizontal stacking1',stacked)

	
	if cv.waitKey(1) & 0xFF==ord('d'):
		break	

cap.release()
cv.destroyAllWindows()


