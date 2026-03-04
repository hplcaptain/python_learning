import cv2

img = cv2.imread("images/sample.jpeg")

height, width = img.shape[:2]

center = (width // 2, height // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1)

rotated = cv2.warpAffine(img, matrix, (width, height))

cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()