import cv2 as cv
# img=cv.imread('images/cat.jpeg')
# cv.imshow('cat',img)
# cv.waitKey(0)

capture=cv.VideoCapture('videos/velo.mp4')
while True:
	isTrue,frame=capture.read()
	cv.imshow('vel',frame)
	if cv.waitKey(20) & 0xFF==ord('d'):
		break
capture.release() 
cv.destroyAllWindows()

cv.waitKey(0)