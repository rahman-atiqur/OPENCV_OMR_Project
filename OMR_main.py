import cv2
import numpy as np

#############################################################
path="image1.jpg"
widthImg=400
heightImg=600
#############################################################

img=cv2.imread(path)
img=cv2.resize(img,(widthImg,heightImg))
############################################################


############################################################


cv2.imshow("Original",img)
cv2.waitKey(0)
