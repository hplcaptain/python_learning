import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype="uint8")

# Rectangle
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)

# Circle
cv2.circle(img, (300, 150), 50, (255, 0, 0), 2)

# Line
cv2.line(img, (50, 300), (450, 300), (0, 0, 255), 2)

# Polygon
points = np.array([[250, 350], [300, 450], [200, 450]])
cv2.polylines(img, [points], True, (255, 255, 0), 2)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()