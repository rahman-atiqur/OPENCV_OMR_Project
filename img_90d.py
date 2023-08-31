import numpy as np
import cv2

# img=cv2.imread('Capture2.jpg')
img=cv2.imread('DSC01983.jpg')
img=cv2.resize(img,(400,400))

rows,cols=img.shape[:2]

src_points=np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
print(src_points)

dst_points=np.float32([[0,0],[cols-1,0],[int(0.33*cols),rows-1],[int(0.66*cols),rows-1]])
print(dst_points)

projective_matrix=cv2.getPerspectiveTransform(src_points,dst_points)

img_output=cv2.warpPerspective(img,projective_matrix,(cols,rows))

cv2.imshow('Org', img)
cv2.imshow('90D', img_output)

cv2.waitKey(0)
cv2.destroyAllWindows()