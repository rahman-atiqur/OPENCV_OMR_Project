import cv2

img_path='OMR_100_new.jpg'
# im = cv2.imread('image1.jpg')
im = cv2.imread(img_path)
cv2.imshow('Original',im)
print(type(im))
# <class 'numpy.ndarray'>

# print(im.shape)
# print(type(im.shape))

# (225, 400, 3)
# <class 'tuple'>

h, w, c = im.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)
# width:   400
# height:  225
# channel: 3

widthImg=1241
heightImg=1754
#############################################################

im=cv2.imread(img_path)
im=cv2.resize(im,(widthImg,heightImg))
cv2.imshow('Resized',im)

h, w, c = im.shape
print('R-width:  ', w)
print('R-height: ', h)
print('R-channel:', c)
cv2.waitKey()


