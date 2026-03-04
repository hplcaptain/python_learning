import cv2

# Read the image from the specified path
image = cv2.imread("images/sample.jpeg")

cv2.imwrite("images/sample_output.jpeg", image)

print("Image has been written to output/sample_output.jpeg")
