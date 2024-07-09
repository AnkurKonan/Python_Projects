import cv2
import numpy


img = cv2.imread('MHA.png')
width = int(img.shape[1] * 50 / 100)
height = int(img.shape[0] * 50 / 100)
size = (width, height)
resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
cv2.imshow('MHA', resized_img)
blank = numpy.zeros(resized_img.shape[:2], dtype='uint8')
cv2.imshow('Blank Image', blank)

circle = cv2.circle(blank.copy(), (resized_img.shape[1] // 2 + 45, resized_img.shape[0] // 2), 100, 255, -1)
rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv2.bitwise_and(circle, rectangle)
cv2.imshow('Half cut circle', weird_shape)

masked = cv2.bitwise_and(resized_img, resized_img, mask=weird_shape)
cv2.imshow('Half cut masked image', masked)
cv2.waitKey(100000)
cv2.destroyAllWindows()
