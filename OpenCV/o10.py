import cv2
import numpy

img = cv2.imread('MHA.png')
width = int(img.shape[1] * 50 / 100)
height = int(img.shape[0] * 50 / 100)
size = (width, height)
resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
cv2.imshow('MHA', resized_img)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

def translate(img, x, y):
    transMat = numpy.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)
  
translated = translate(resized_img, -100, 100)
cv2.imshow('Translated', translated)

def rotate(resized_img, angle, rotPoint=None):
    (height, width) = resized_img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(resized_img, rotMat, dimensions)

rotated = rotate(resized_img, -45)
cv2.imshow('Rotated', rotated)

rotated_rotated = rotate(resized_img, -90)
cv2.imshow('Rotated Rotated', rotated_rotated)

flip = cv2.flip(resized_img, -1)
cv2.imshow('Fliping Image', flip)

cv2.waitKey(20000)
