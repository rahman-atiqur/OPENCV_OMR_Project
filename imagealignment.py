import cv2
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt

# Read reference
refImage="OMR_100.jpg"
print('Reference Image: ', refImage)
img1=cv2.imread(refImage,cv2.IMREAD_COLOR)
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

# Read image to be aligned
scannedImage="OMR_100_skewed.jpg"
print("Reading Image to be aligned: ",scannedImage)
img2=cv2.imread(scannedImage,cv2.IMREAD_COLOR)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

#Display Image
plt.figure(figsize=[20,10])
plt.subplot(121);plt.axis('off');plt.imshow(img1);plt.title('Original Image')
plt.subplot(122);plt.axis('off');plt.imshow(img2);plt.title('Scanned Image')


#showing image
# cv2.imshow("Reference Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()