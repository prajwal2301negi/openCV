import cv2

# Initialize webcam
webcam = cv2.VideoCapture(0)  # Use '0' for the default webcam

if not webcam.isOpened():
    print("Error: Could not open video capture device")
else:
    while True:
        ret, frame = webcam.read()  # Read a frame from the webcam

        # Check if the frame was successfully captured
        if not ret or frame is None:
            print("Error: Failed to capture frame")
            break

        # Display the frame
        cv2.imshow('frame', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            
             # This waits for 1 millisecond for a key press. If no key is pressed within that time, the program continues.

             # Higher value in waitKey() (e.g., 40 ms): Slower video playback or reduced frame rate.

             # Lower value in waitKey() (e.g., 1 ms): Faster video playback or smoother real-time performance.

             # In summary, cv2.waitKey(1) is for fast real-time processing, while cv2.waitKey(40) ensures video frames are displayed at approximately 25 fps.
            break

    # Release the video webcamture and close any OpenCV windows
    webcam.release()
    cv2.destroyAllWindows()
