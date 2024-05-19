# Smart Question Paper:

''' Problem Statement: Consider the attached image.
Use the OpenCV contour finding function to find the centroid
and area of every contour in the image and print it. '''

import cv2
import numpy as np

image = cv2.imread('INSERT IMAGE PATH', cv2.IMREAD_GRAYSCALE)

if image is None:
    raise ValueError("Image not found. Please check the path.")

blurred = cv2.GaussianBlur(image, (5, 5), 0)

_, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:

    area = cv2.contourArea(contour)
    
    M = cv2.moments(contour)
    
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    else:
        cx, cy = 0, 0
    
    print(f'Contour: Centroid = ({cx}, {cy}), Area = {area}')

output_image = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

for contour in contours:
    
    M = cv2.moments(contour)
    
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
    else:
        cx, cy = 0, 0
    
    # Draw the contour and centroid
    cv2.drawContours(output_image, [contour], -1, (0, 255, 0), 2)
    cv2.circle(output_image, (cx, cy), 5, (255, 0, 0), -1)

cv2.imshow('Image with Centroids', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
