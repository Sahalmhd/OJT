import cv2
import numpy as np

# Read the image
image = cv2.imread('trafic_image.jpg')
if image is None:
    print('could not read the image')
    exit()

# Convert to grayscale
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(grey_image, (5, 5), 0)

# Detect edges using Canny
edges = cv2.Canny(blurred_image, 50, 150)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Display the grayscale image
cv2.imshow('Grayscale Image', grey_image)
cv2.waitKey(0)

# Display the blurred image
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)

# Display the edges image
cv2.imshow('Edges Image', edges)
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
