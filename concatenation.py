# Displaying image
# Loading images
image1=cv2.imread("C:/Users/ASUS/OneDrive/Pictures/f1 stickers/cl helmet.png",0)
image2=cv2.imread("C:/Users/ASUS/OneDrive/Pictures/f1 stickers/cs helmet.png",0)
image3=cv2.imread("C:/Users/ASUS/OneDrive/Pictures/f1 stickers/cs and cl.png",0)

# displaying each images
# image 1
cv2.imshow("picture1", image1)
# image 2
cv2.imshow("picture2", image2)
# image 3
cv2.imshow("picture3", image3)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Concatenating images
# resizing all pictures to be the same size
image2=cv2.resize(image2, (image1.shape[1],image1.shape[0]))
image3=cv2.resize(image3, (image1.shape[1],image1.shape[0]))

# concatenating the images horizontally
hconcate = cv2.hconcat([image1, image2, image3])
displayImage(hconcate)
