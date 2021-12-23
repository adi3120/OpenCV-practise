import cv2 as cv

def getRes():
	print("width = ",capture.get(3),"\n","height = ",capture.get(4))

def setRes(w,h):
	#ONLY for LIVE videos, wont work for standalone video files
	capture.set(3,w)
	capture.set(4,h)

def playVid(video):
	while True:
		isTrue,frame=video.read()
		cv.imshow('vel',frame)
		if cv.waitKey(20) & 0xFF==ord('d'):
			break
	capture.release()
	cv.destroyAllWindows()

capture=cv.VideoCapture('videos/velo.mp4')

getRes()

setRes(300,300)

getRes()

playVid(capture)




