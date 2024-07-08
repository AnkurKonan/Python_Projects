#Thresholding
import cv2
import numpy

img = cv2.imread('luffy.jpeg')
width = int(img.shape[1] * 50 / 100)
height = int(img.shape[0] * 50 / 100)
size = (width, height)
resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY )
cv2.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV )
cv2.imshow('Simple Thresholded Inverse', thresh_inv)

adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)
cv2.waitKey(50000)
