import cv2
import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams['figure.figsize'] = [10, 3]

# methods to display images (using matplotlib)
# to display one image 
def displayImage (img):
    plt.imshow(img, cmap='gray')
    plt.show()

# to display 2 images 
def displayImages(img1,img2):
    fig= plt.figure(figsize=(10,20))
    fig.add_subplot(1, 2, 1)
    plt.imshow(img1, cmap='gray')
    plt.axis('off')
    plt.title("First")
    
    fig.add_subplot(1, 2, 2)
    plt.imshow(img2, cmap='gray')
    plt.axis('off')
    plt.title("Second")
    plt.show()

# Binary Picture
binary_picture = np.zeros((300,300), dtype=np.uint8)
displayImage(binary_picture)
# drawing a circle
circle1 = np.zeros_like(binary_picture, dtype=np.uint8)
center =(140,120)
radius =70
circle1 = cv2.circle(circle1, center, radius, 255, -1)
displayImage(circle1)

# drawing another circle 
circle2 = np.zeros_like(binary_picture, dtype=np.uint8)
center =(200,190)
circle2=cv2.circle(circle2, center, radius, 255, -1)
displayImage(circle2)

# display both circles together 
circles = cv2.bitwise_or(circle1,circle2)
displayImage(circles)

# draw 2 squares 
square1 = np.zeros_like(binary_picture,dtype=np.uint8)
square1[80:180, 200:] = 255
#square1 = cv2.bitwise_not(square1)
#displayImage(square1)

square2=  np.zeros_like(binary_picture,dtype=np.uint8)
square2[180:,100:200]=255

# display the two squares together
squares = cv2.bitwise_or(square1,square2)
squares= cv2.bitwise_not(squares)
displayImage(squares)

# display everything together
binary_picture=cv2.bitwise_and(circles,squares)
displayImage(binary_picture)
