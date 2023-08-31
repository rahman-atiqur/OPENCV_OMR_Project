import cv2
import numpy as np
import tkinter as tk


prevX,prevY=-1,-1
def printCoordinate(event, x, y, flags, params):
    global prevX,prevY,img
    # if event==cv2.EVENT_LBUTTONDOWN:
    
    if event==cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img,(x,y),3,(255,255,255),-1)
        # strXY='('+str(x)+','+str(y)+')'
        # font=cv2.FONT_HERSHEY_PLAIN
        # cv2.putText(img,strXY,(x+10,y-10),font,1,(255,255,255))
        if prevX==-1 and prevY==-1:
            prevX,prevY=x,y
        else:
            cv2.rectangle(img,(prevX,prevY),(x,y),(0,255,0),2)
            prevX,prevY=-1,-1

        cv2.imshow("image",img)

# img = np.zeros((800,800,3),dtype=np.uint8)
img=cv2.imread('OMR_100.jpg')
img=cv2.resize(img,(1241,1754))
cv2.imshow("image",img)
cv2.setMouseCallback("image", printCoordinate)
cv2.waitKey()
cv2.destroyAllWindows()