import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'whiteBoard.png'))

# Line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)
# Points, Color, Thickness


# Rectangle
cv2.rectangle(img, (10, 50), (30, 60), (0,0, 255), 5)
# UpperLeft, BottomRight, Color, Thickness
# With thickness = -1, rectangle get filled with color


# Circle
cv2.circle(img, (50, 80), 15, (255, 0, 0), 10)
# Center, Radius, Color, Thickness


# Text
cv2.putText(img, 'hello world', (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)
# Points, FontName, Size, Color, Thickness


cv2.imshow('img', img)
cv2.waitKey(0)