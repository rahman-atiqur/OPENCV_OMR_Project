import cv2

image = cv2.imread('OMR_60.jpg')
ww,hh,cc=image.shape

sub_image = image[0:0+hh, 0:0+95]

blur = cv2.pyrMeanShiftFiltering(sub_image, 11, 21)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
i=0
for c in cnts:
    x1,y1 = c[0][0]
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        i+=1
        x,y,w,h = cv2.boundingRect(approx)
        cv2.rectangle(image,(x,y),(x+w,y+h),(36,255,12),1)

j=0
for c in cnts:
    x1,y1 = c[0][0]
    j+=1
    cv2.putText(image, str(i-j+1), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)


cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()