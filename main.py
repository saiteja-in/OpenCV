import numpy as np
import cv2

img = cv2.imread('assets/hexagon.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.089, 10)
corners = np.int0(corners)

for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Iterate through each corner to find and draw lines to its two nearest neighbors
for i in range(len(corners)):
    corner1 = tuple(corners[i][0])
    distances = []

    for j in range(len(corners)):
        if i != j:
            corner2 = tuple(corners[j][0])
            distance = euclidean_distance(corner1, corner2)
            distances.append((distance, corner2))
    
    # Sort distances and select the two nearest corners
    distances.sort(key=lambda x: x[0])
    nearest_corners = [distances[0][1], distances[1][1]]

    # Draw lines to the two nearest corners
    color = (0, 255, 255)  # Yellow color in BGR
    thickness = 2  # Increased thickness
    
    for nearest_corner in nearest_corners:
        cv2.line(img, corner1, nearest_corner, color, thickness)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()