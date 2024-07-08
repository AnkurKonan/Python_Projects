import cv2

#Basic Functions
img = cv2.imread('MHA.png')
width = int(img.shape[1] * 50 / 100)
height = int(img.shape[0] * 50 / 100)
size = (width, height)
resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
cv2.imshow('MHA', resized_img)

grayscale_image = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale', grayscale_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

blured_image = cv2.GaussianBlur(resized_img, (8,8), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blured_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

canny_image = cv.Canny(resized_img, 125, 175)
cv.imshow('Canny', canny_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

dilated_image= cv2.dilate(resized_img, (7,7), iterations=3)
cv2.imshow('Dilated', dilated_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

eroded_image = cv2.erode(resized_img, (7,7), iterations=3)
cv2.imshow('Eroded', eroded_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()

croping_image = img[50:200, 200:400]
cv.imshow('Cropped', croping_image)



