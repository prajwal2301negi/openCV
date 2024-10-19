import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

resized_img = cv2.resize(img, (640, 214)) # we pass height and width in reciprocal.

print(img.shape)  # (427, 640, 3)
print(resized_img.shape) # (214, 640, 3)

cv2.imshow('img', img) 
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)