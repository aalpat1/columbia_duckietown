import numpy as np
import cv2

def filtered_image(image, lbound, ubound):
    mask = cv2.inRange(image, lbound, ubound)
    return mask

def find_left_lane(image):
    yellow_lbound = np.array([28, 150, 100], dtype = np.uint8)
    yellow_ubound = np.array([32, 255, 255], dtype = np.uint8)
    mask = filtered_image(image, yellow_lbound, yellow_ubound)
    return mask

def find_right_lane(image):
    white_lbound = np.array([0,0,200], dtype = np.uint8)
    white_ubound = np.array([255,70,255], dtype = np.uint8)
    mask = filtered_image(image, white_lbound, white_ubound)
    return mask
    
def find_stop_sign(image):
    orange_lbound = np.array([8, 100, 100], dtype = np.uint8)
    orange_ubound = np.array([12, 255, 255], dtype = np.uint8)
    mask = filtered_image(image, orange_lbound, orange_ubound)
    return mask

def erode_and_dilate(image):
	# Perform erosion + dilation
	kernel = np.ones((5,5), np.uint8)
	image = cv2.erode(image, kernel, iterations=1)
	image = cv2.dilate(image, kernel, iterations=1)
	return image
