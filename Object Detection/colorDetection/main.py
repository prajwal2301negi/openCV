# Building Color Detector using python and openCV. Without the use of tensorflow, keras or yolo.

import cv2
from PIL import Image

from util import get_limits

yellow = [0, 255, 255] # yellow in BGR colorspace

cap = cv2.VideoCapture(0) # webCam
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    # the 2 number we pass, determine all the pixel in between

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox() # for bounting box

    if bbox is not None:
        x1, y1, x2, y2 = bbox
    
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # print(bbox)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()