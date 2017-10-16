from gopigo import *
import io
import picamera # imports the driver to access robot's camera
import numpy as np
import lane_filter as lf
import cv2

camera = picamera.PiCamera()
time.sleep(5) # Let camera warm up to improve brightness
camera.resolution = (320, 240)

# take an image
camera.capture('image.jpg') # Saves imaage to current path
img = cv2.imread('image.jpg', 1) # Converts image to opencv image
image_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Now, we'll apply a mask to the image
left_lane = lf.find_left_lane(image_hsv)
right_lane = lf.find_right_lane(image_hsv)
stop_sign = lf.find_stop_sign(image_hsv)

#show image
cv2.imwrite("left_lane.jpg", left_lane)
cv2.imwrite("right_lane.jpg", right_lane)
cv2.imwrite("stop_sign.jpg", stop_sign)

