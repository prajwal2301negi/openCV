import os
import cv2

# Read Video 
video_path = os.path.join('.', 'data', 'monkey.mp4')
video = cv2.VideoCapture(video_path)

# Visualize Video

ret = True
while ret:
    ret, frame = video.read()  # ret -> boolean frame, frame -> video frame
    # After video is seen by us, ret = False

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40) # wait for 40ms

# To release the memory
video.release()
cv2.destroyAllWindows()        
