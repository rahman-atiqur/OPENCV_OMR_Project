import cv2
import numpy as np
import tkinter as tk

from tkinter import *
from tkinter import ttk
from scipy.ndimage import interpolation as inter

from tkinter import messagebox
# from PIL import ImageTk, Image


def timerCount(img):   

    image = cv2.imread(img)
    hh,ww,cc=image.shape

    sub_image = image[0:0+hh, 0:0+85]

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
        cv2.putText(image, str(i-j), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)


    cv2.imshow('thresh', thresh)
    cv2.imshow('image', image)

    cv2.imwrite('template.jpg',image)

    return 'template.jpg'

###############
# # De-skewed
def correctSkew(image):

    delta=1
    limit=5
    def determine_score(arr, angle):
        data = inter.rotate(arr, angle, reshape=False, order=0)
        histogram = np.sum(data, axis=1, dtype=float)
        score = np.sum((histogram[1:] - histogram[:-1]) ** 2, dtype=float)
        return histogram, score

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 

    scores = []
    angles = np.arange(-limit, limit + delta, delta)
    for angle in angles:
        histogram, score = determine_score(thresh, angle)
        scores.append(score)

    best_angle = angles[scores.index(max(scores))]

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
    corrected = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, \
            borderMode=cv2.BORDER_REPLICATE)

    de_skewed='de_skewed.jpg'
    cv2.imwrite(de_skewed,corrected)

    # return best_angle, corrected
    return de_skewed
    
    #######################################################################################