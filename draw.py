import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
#----------------------------------------------------------------------------------------------------

#1. Paint image a certain color

blank[:]=0,255,0

cv.imshow('green',blank)

blank[:]=0,0,255

cv.imshow('red',blank)
#----------------------------------------------------------------------------------------------------

#2. Make a box

blank[:]=0,0,0

blank[200:300,300:400]=0,0,255

cv.imshow('box',blank)
#----------------------------------------------------------------------------------------------------

#3. Make a rectangle

blank[:]=0,0,0

cv.rectangle(blank,(0,0),(400,400),(0,255,255))

cv.imshow('Rectangle hollow',blank)

blank[:]=0,0,0

cv.rectangle(blank,(0,0),(400,400),(0,255,255),thickness=-1)

cv.imshow('Rectangle filled',blank)
#----------------------------------------------------------------------------------------------------

#4. Make a circle

blank[:]=0,0,0

cv.circle(blank,(250,250),100,(100,150,250))

cv.imshow('Circle hollow',blank)

blank[:]=0,0,0

cv.circle(blank,(250,250),100,(100,150,250),thickness=-1)

cv.imshow('Circle filled',blank)
#----------------------------------------------------------------------------------------------------
#5. Draw a line

blank[:]=0,0,0

cv.line(blank,(0,0),(250,250),(0,0,255),thickness=10)

cv.imshow('Line',blank)
#----------------------------------------------------------------------------------------------------

#6. Draw Text on image

blank[:]=0,0,0

cv.putText(blank,'Aditya made this',(50,100),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,0),thickness=5)

cv.imshow('Text on image',blank)

cv.waitKey(0)