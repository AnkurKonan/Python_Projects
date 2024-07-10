import cv2
import numpy

img = cv2.imread('MHA.png')
width = int(img.shape[1] * 50 / 100)
height = int(img.shape[0] * 50 / 100)
size = (width, height)
resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
cv2.imshow('MHA', resized_img)

img = cv2.imread('MHA', resized_img)
cv2.imshow('MHA', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('LAB --> BGR', lab_bgr)
cv2.waitKey(100000)
