import cv2
import numpy as np

# Define a kernel for morphological operations
kernel = np.ones((3, 3), dtype=np.uint8)
image = cv2.imread('images/sample.jpeg')
erosion = cv2.erode(image, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow('Erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()


                   