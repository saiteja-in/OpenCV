import numpy as np
import cv2
img=cv2.imread('assets/chessboard.png')
img=cv2.resize(img,(0,0),fx=0.75,fy=0.75)  #fits the image to the scree, it just resizes the image doesnt crop it
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converts the given image into gray scale]
corners = cv2.goodFeaturesToTrack(img, 100, 0.01, 10)
corners=np.int0(corners)
for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),5,(255,0,0),-1)



cv2.imshow('Frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()