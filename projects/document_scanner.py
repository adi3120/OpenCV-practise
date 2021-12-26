from typing import BinaryIO
import cv2 as cv
import numpy as np


widthImg=480
heightImg=640

url="http://192.168.43.120:8080/video"

cap=cv.VideoCapture(url)
cap.set(3,640)
cap.set(4,480)


def preProcessing(img):
	imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
	imgBlur=cv.GaussianBlur(imgGray,(5,5),1)
	imgCanny=cv.Canny(imgBlur,200,200)
	kernel= np.ones((5,5))
	imgDial=cv.dilate(imgCanny,kernel,iterations=2)
	imgThres=cv.erode(imgDial,kernel,iterations=1)

	return imgThres

def getContours(img):
	biggest=np.array([])
	maxArea=0
	contours,hierarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

	for cont in contours:
		area=cv.contourArea(cont)
		if area>500:
			peri=cv.arcLength(cont,True)
			approx=cv.approxPolyDP(cont,0.02*peri,True)
			if area>maxArea and len(approx)==4:
				biggest=approx
				maxArea=area
	cv.drawContours(imgContour,biggest,-1,(255,0,0),20)
	return biggest

def reorder(myPoints):
	myPoints=myPoints.reshape((4,2))
	myPointsNew=np.zeros((4,1,2),np.int32)

	add=myPoints.sum(1)

	myPointsNew[0]=myPoints[np.argmin(add)]
	myPointsNew[3]=myPoints[np.argmax(add)]

	diff=np.diff(myPoints,axis=1)

	myPointsNew[1]=myPoints[np.argmin(diff)]
	myPointsNew[2]=myPoints[np.argmax(diff)]

	return myPointsNew



def getWarp(img,biggest):

	biggest=reorder(biggest)
	pts1=np.float32(biggest)
	pts2=np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])

	matrix=cv.getPerspectiveTransform(pts1,pts2)
	imgOutput=cv.warpPerspective(img,matrix,(widthImg,heightImg))

	imgCropped=imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
	imgCropped=cv.resize(imgCropped,(widthImg,heightImg))
	return imgCropped

while True:
	_,img=cap.read()
	img=cv.resize(img,(widthImg,heightImg))
	imgContour=img.copy()
	imgThres=preProcessing(img)
	biggest=getContours(imgThres)
	if biggest.size!=0:

		imgWarped=getWarp(img,biggest)
		cv.imshow('Image Result',imgWarped)

	if cv.waitKey(20) & 0xFF == ord('d'):
		break

cap.release()
cv.destroyAllWindows()
