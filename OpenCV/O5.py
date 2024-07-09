import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('MHA.png')
width = int(img.shape[1] * 50 / 100)
height = int(img.shape[0] * 50 / 100)
size = (width, height)
resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

cv2.imshow('MHA', resized_img)

blank = np.zeros(resized_img.shape[:2], dtype='uint8')
mask = cv2.circle(blank, (resized_img.shape[1]//2, resized_img.shape[0]//2), 100, 255, -1)

masked = cv2.bitwise_and(resized_img, resized_img, mask=mask)
cv2.imshow('Mask', masked)

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv2.calcHist([resized_img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()
cv2.waitKey(100000)
cv2.destroyAllWindows()
