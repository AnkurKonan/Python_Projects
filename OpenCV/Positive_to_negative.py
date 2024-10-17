import cv2
import os

image_path = 'text.png' 
if not os.path.exists(image_path):
    print(f"Error: The file '{image_path}' does not exist!")
    exit()

img = cv2.imread(image_path)

if img is None:
    print("Error: Unable to load the image. Please check the file path and format.")
    exit()

negative_img = 255 - img

cv2.imshow('Original Image', img)
cv2.imshow('Negative Image', negative_img)

cv2.waitKey(15000)  
cv2.destroyAllWindows()

cv2.imwrite('negative_image.jpg', negative_img)
