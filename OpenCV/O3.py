import cv2
import numpy

blank = numpy.zeros((400,400), dtype='uint8')
rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv2.imshow('Rectangle', rectangle)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)
cv2.imshow('Circle', circle)

And = cv2.bitwise_and(rectangle, circle)
cv2.imshow('AND', And)

Or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('OR', Or)

Not = cv2.bitwise_not(circle)
cv2.imshow('NOT', Not)

Xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('XOR', Xor)
cv2.waitKey(100000)
