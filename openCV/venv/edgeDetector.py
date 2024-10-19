import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'basketball.webp'))

img_edge = cv2.Canny(img, 100, 200)
# Hysteresis Thresholding
# The values 100 and 200 are threshold values (maxBal and minVal)
# 400 and 500 as values --> less details will be captured.

img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype = np.int8)) 
# using dilate now  ---> Thick edges.
# can pass numpy_array = (3,3)

img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype = np.int8)) 
# using erode now.


cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)