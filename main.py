import cv2
img = cv2.imread('assets/logo.jpg',-1)
print(img.shape[1])
print(img.shape)#(995, 1000, 3)


# img.shape returns the dimensions of the image in the form of a tuple (height, width). Therefore, img.shape[1] specifically refers to the width of the image.

# cv2.imshow('Image', img)
# cv2.waitKey(0)