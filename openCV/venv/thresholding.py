# Thresholding --->
# Converting image to Binary

# Use with images containing Text.

# Different Types of Thresholding --->
# BINARY, BINARY_INV, TRUNIC, TOREZO, TOREZO_INV

# Some of these ways, you will not be creating a binary image but creating binary images is the most common use case of thresholding.

import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thres = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# adaptive --> will adjust by itself

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)  
# pixel below 80 will be taken as 0 and above will be taken as 255.

cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.imshow('adaptive_thres', adaptive_thres)
cv2.waitKey(0)