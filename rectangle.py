import cv2
import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams['figure.figsize'] = [10, 3]
# load image
picture = cv2.imread("C:/Users/ASUS/OneDrive/Pictures/pic1.jpeg",0)
displayImage(picture)

# other data about the rectangle 
color =(0,0,0)
thick=2

# points of the rectangle
start= None  # top left corner
end = None   # bottom right corner

image_w_rect =None
def draw_rect(event, x, y, flags, param):
    global start, end, image_w_rect

    if event == cv2.EVENT_LBUTTONDOWN:
        if start is None:
           start = (x,y)
           print(start)
        elif end is None:
           end=(x,y)
           print(end)
        
        minX= min(start[0],end[0])
        maxX= max(start[0], end[0])

        minY=min(start[1], end[1])
        maxY=max(start[1], end[1])

        start =(minX, minY)
        end = (maxX, maxY)
        
        
        
        # new picture with the drawn triangle
        image_w_rect=cv2.rectangle(picture, start, end, color, thick)

# driver program
picture = cv2.imread("C:/Users/ASUS/OneDrive/Pictures/pic1.jpeg",0)
cv2.namedWindow('Rectangle')
cv2.setMouseCallback('Rectangle', draw_rect)

while(1):
   cv2.imshow('Rectangle', picture)
   if image_w_rect is not None:
      cv2.imshow('drawn', picture)
   key = cv2.waitKey(1)
   if key == 27:  # esc key
      break
cv2.destroyAllWindows()
