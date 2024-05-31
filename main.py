import cv2
import random
img = cv2.imread('assets/logo.jpg',-1)
print(img.shape[1])
print(img.shape)#(995, 1000, 3(channels))

for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

  
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag  
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# blue green red
# [255,0,0]means only blue pixel is present
# [255,255,0] both blue and gree are present