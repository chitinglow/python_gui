import cv2
import numpy as np

# Read video file
new_capture = cv2.VideoCapture('fun.mp4')

# Check if the file opened successfully
if (new_capture.isOpened() == False):
    print("Error for opening the video file")

# Reading the video to complete
while (new_capture.isOpened()):
    ret, frame = new_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release when everything is completed
new_capture.release()
cv2.destroyAllWindows()  # close all frames