import cv2
import numpy as np

img = cv2.imread('OMR_60s.jpg')
# img = cv2.imread('input/OMR_100_skewed.jpg')
# img = cv2.imread('input/document.jpg')

# Pixel values in the original image
input_points = np.float32([[83, 18], [342, 53], [14, 389], [295, 436]])
# input_points = np.float32([[83, 18], [342, 53], [14, 389], [295, 436]])

# Output image size
# width = 400
# height = int(width * 1.414)  # for A4
width, height, c =img.shape

# Desired points values in the output image
converted_points = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Perspective transformation
matrix = cv2.getPerspectiveTransform(input_points, converted_points)
img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Original', img)
cv2.imshow('Warped perspective', img_output)

cv2.imwrite('output/document.jpg', img_output)

cv2.waitKey(0)
