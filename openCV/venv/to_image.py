import cv2
import os


# Read Image
image_path = os.path.join('.', 'data', 'bird.jpg')

img = cv2.imread(image_path)

# Write Image
cv2.imwrite(os.path.join('.', 'bird_out.jpg'), img)


# Visualize Image
cv2.imshow('image', img)
cv2.waitKey(0)   # To wait unitl we press a key, No of millisec we want openCV to keep the file open.