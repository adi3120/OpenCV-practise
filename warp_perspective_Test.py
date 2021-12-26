import cv2 as cv
import numpy as np

img=cv.imread('images/card.jpg')
pt1=[101,50]
pt2=[304,77]
pt3=[48,285]
pt4=[271,314]



oldPoints=np.float32([pt1,pt2,pt3,pt4])
newPoints=np.float32([[0,0],[480,0],[0,640],[480,640]])
for points in oldPoints:
	points=np.int32(points)
	cv.circle(img,points,6,(255,0,0),4)

matrix=cv.getPerspectiveTransform(oldPoints,newPoints)
imgResult=cv.warpPerspective(img,matrix,(480,640))
cv.imshow("Image",img)
cv.imshow("Image warped",imgResult)

cv.waitKey(0)