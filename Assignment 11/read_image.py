import cv2

# Read the image from the specified path
image = cv2.imread("images/sample.jpeg")

cv2.imshow("Sample Image", image)
cv2.waitKey(0)  
cv2.destroyAllWindows()