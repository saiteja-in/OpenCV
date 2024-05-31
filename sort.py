import numpy as np
import cv2

# Load and preprocess the image
img = cv2.imread('assets/hexagon.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10)
corners = np.int0(corners)

# Convert corners to a list of tuples and sort them by y-coordinate
corners_list = [tuple(corner.ravel()) for corner in corners]
sorted_corners = sorted(corners_list, key=lambda x: x[1])

# Print and draw sorted corners
for i, (x, y) in enumerate(sorted_corners):
    print(f"Corner {i}: ({x}, {y})")
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# Display the image with sorted corners
cv2.imshow('Sorted Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
