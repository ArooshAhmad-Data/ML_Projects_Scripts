import cv2
import numpy as np

# Load the image
img = cv2.imread('image2.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_copy = gray .copy()

# Find all pixels with the gray level 100
indices = gray == 66

# Set those pixels to white
img_copy[indices] = 255


# edges = cv2.Canny(img, threshold1=30, threshold2=100)

# # Adjust contrast and brightness
# img = cv2.convertScaleAbs(img, 10, 1)
#
# # Equalize the histogram of the grayscale image
# img_eq = cv2.equalizeHist(img)
#
# # Threshold the image: Set to white all pixels that are not completely white
# _, img_thresh = cv2.threshold(img_eq, 254, 255, cv2.THRESH_BINARY)
#
# # Invert the image: Convert white to black and black to white
# img_inverted = cv2.bitwise_not(img_thresh)
#
# # Resize the image
# img_resized = cv2.resize(img_inverted, (500,700))

# Display the image
cv2.imshow("Image", cv2.resize(img_copy, (500,700)))
cv2.waitKey(0)
cv2.destroyAllWindows()
