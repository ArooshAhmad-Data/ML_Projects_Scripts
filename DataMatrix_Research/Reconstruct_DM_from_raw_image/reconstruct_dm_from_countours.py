import numpy as np
import cv2

"""
The script converts the image to binary and try to recinstruct it making a data matrix from it.
"""

path = "Images\img1.jpg" # Path to the input image

img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output_img = np.ones_like(img) * 255

centroids = []
for contour in contours:
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        centroids.append((cX, cY))

for i in range(len(centroids)):
    for j in range(i + 1, len(centroids)):
        cv2.drawContours(output_img, [contours[i]], -1, (0, 0, 0), thickness=cv2.FILLED)
        
        cX1, cY1 = centroids[i]
        cX2, cY2 = centroids[j]

        distance = np.sqrt((cX1 - cX2) ** 2 + (cY1 - cY2) ** 2)

        width1 = cv2.boundingRect(contours[i])[2]
        width2 = cv2.boundingRect(contours[j])[2]
        avg_width = ((width1 + width2) / 2)*2.5

        if distance < avg_width:
            cv2.rectangle(output_img, (cX1, cY1), (cX2, cY2), (0, 0, 0), 7,lineType=cv2.LINE_AA)

cv2.imshow("Image with Dynamically Connected Centroids", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
