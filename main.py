import cv2
img = cv2.imread('assets/logo.png',1)
img=cv2.resize(img,(1024,1024),fx=0.5,fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('assets/new_img.jpg', img)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()