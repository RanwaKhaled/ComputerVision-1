import cv2
import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams['figure.figsize'] = [10, 3]
# load image
image = cv2.imread("C:/Users/ASUS/OneDrive/Pictures/black n white flower.jpg",0)
# display image
displayImage(image)
# Reflecting the image
# flip horizontally
h_flip= cv2.flip(image, 0) 
# flip vertically
v_flip=cv2.flip(image, 1)

# displaying fipped pics 
displayImages(h_flip, v_flip)
# Rotating an image 
# Rotating 90 degrees
# clockwise
rotated_cw=cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) 
# anti-clockwise
rotated_acw=cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
# Rotating 180 degrees
rotated=cv2.rotate(image, cv2.ROTATE_180)
# displaying rotated images
# 90 deg
displayImages(rotated_cw,rotated_acw)
# 180 deg
displayImage(rotated)
