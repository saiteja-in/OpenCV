import cv2
import numpy as np

def detect_color_dot(image, color_lower, color_upper):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create a mask for the specified color
    mask = cv2.inRange(hsv, color_lower, color_upper)

    # Find contours in the masked image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, get the largest one
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(max_contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            return (cx, cy)
    return None

def detect_center(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threshold = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(max_contour)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            return (cx, cy)
    return None

def calculate_angle(center, point1, point2):
    vector1 = np.array([point1[0] - center[0], point1[1] - center[1]])
    vector2 = np.array([point2[0] - center[0], point2[1] - center[1]])

    unit_vector1 = vector1 / np.linalg.norm(vector1)
    unit_vector2 = vector2 / np.linalg.norm(vector2)

    dot_product = np.dot(unit_vector1, unit_vector2)
    angle = np.arccos(dot_product)

    return np.degrees(angle)

# Read the image
image = cv2.imread('assets/fin.jpg')

# Define the color ranges for red and green in HSV
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

# Detect red and green dots
red_dot = detect_color_dot(image, lower_red, upper_red)
green_dot = detect_color_dot(image, lower_green, upper_green)

# Detect the center of the hexagon
center = detect_center(image)

if center is not None and red_dot is not None and green_dot is not None:
    print(f"Center: {center}")
    print(f"Red dot: {red_dot}")
    print(f"Green dot: {green_dot}")

    # Calculate the angle between the dots
    angle = calculate_angle(center, red_dot, green_dot)
    print(f"Angle between the dots: {angle:.2f} degrees")

    # Draw the dots and the center
    cv2.circle(image, red_dot, 5, (0, 0, 255), -1)
    cv2.circle(image, green_dot, 5, (0, 255, 0), -1)
    cv2.circle(image, center, 5, (0, 0, 0), -1)

    # Show the image with annotations
    cv2.imshow('Detected Dots and Center', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Detection failed.")
