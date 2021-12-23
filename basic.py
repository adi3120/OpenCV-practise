import cv2 as cv
img=cv.imread('images/cat.jpeg')
cv.imshow('cat',img)

#1.Making the image gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('catGray',gray)

#2. BLur image
img=cv.imread('images/house.jpg')
cv.imshow('House normal',img)

blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('blur house',blur)

#3. Edge detection
canny=cv.Canny(img,125,175)
cv.imshow('Edges',canny)

#4 resize image
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized image',resized)

#5. Cropping
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)