import cv2
import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams['figure.figsize'] = [10, 3]
flower = cv2.imread("C:/Users/ASUS/OneDrive/Pictures/threshold.jpg",0)
displayImage(flower)
# TO ZERO threshold
# threshold value 70
thresh1= flower.copy()
thresh1[thresh1<70] = 0

# to zero inverse
thresh2 = flower.copy()
thresh2[thresh2>70]=0

displayImages(thresh1, thresh2)
