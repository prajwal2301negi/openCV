import os

import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

print(img.shape)  # (427, 640, 3)

cropped_img = img[320:640, 420:840] # Keeping middle part only.
print(cropped_img.shape) # (107, 220, 3)

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)