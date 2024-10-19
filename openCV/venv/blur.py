import os
import cv2

# If we are blurring, we are replacing every pixel by the average of all the other pixels which are around it


# Types --->
# 1 .blur()
# 2 .GaussianBlur()
# 3 .medianBlur()
# 4 .bilateralFilter()


img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

k_size = 7  # if equal to 70, then blur intensity also increases.

# 1 .blur()
img_blur = cv2.blur(img, (k_size, k_size)) 
# Passing 2 parameters -> image and blur_size.

# 2 .gaussian_blur()
img_gaussianBlur = cv2.GaussianBlur(img, (k_size, k_size), 3)

# 3 .median_blur()
img_medianBlur = cv2.medianBlur(img, k_size)
# helps in reducing noise


cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussianBlur', img_gaussianBlur)
cv2.imshow('img_medianBlur', img_medianBlur)
cv2.waitKey(0)