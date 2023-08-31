
import numpy as np
import cv2

# img = cv2.imread('image1.jpg', 0)
# template = cv2.imread('Capture2.jpg', 0)
img = cv2.resize(cv2.imread('image1.jpg', 0), (0, 0), fx=0.2, fy=0.5)
template = cv2.resize(cv2.imread('Capture2.jpg', 0), (0, 0), fx=0.2, fy=0.5)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

print(h,w)
print(methods)
# methods=methods[0] 
# This is one among the above which works perfectly

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print(min_val, max_val, min_loc, max_loc)
    # print(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    # print(location)
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location,bottom_right, 0, 1)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()