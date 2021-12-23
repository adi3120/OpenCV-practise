
import cv2 as cv

def rescale(frame,scale=0.75):
	#Use this for images please
	width=int(frame.shape[1]*scale)
	height=int(frame.shape[0]*scale)
	dimensions=(width,height)

	return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(w,h):
	#use this for videos please
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

# img=cv.imread('images/cat.jpeg')
# cv.imshow('cat',img)


# img_scaled=rescale(img,0.2)
# cv.imshow('cat_resized',img_scaled)



changeRes(1280,720)
# playVid(resizedVid)
playVid(capture)

