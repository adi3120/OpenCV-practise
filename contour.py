import cv2 as cv
 
orgImg=cv.imread('images/house.jpg')

img=cv.resize(orgImg,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('house',img)

blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur house',blur)

gray=cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

canny=cv.Canny(gray,125,175)
cv.imshow('Canny edges',canny)

contours, hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours found')

cv.waitKey(0)