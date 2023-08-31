import cv2
import numpy as np
import tkinter as tk

from tkinter import *
from tkinter import ttk
from scipy.ndimage import interpolation as inter

from tkinter import messagebox
from PIL import ImageTk, Image


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
# Timer line count

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


    # cv2.imshow('thresh', thresh)
    # cv2.imshow('image', image)

  
    cv2.imwrite('template.jpg',image)

    return 'template.jpg'

#######################################################################################
# Region Selection

def selectArea(root,mycanvas,path):
    topx, topy, botx, boty = 0, 0, 0, 0
    # rect_id = ""
    path = path
    canvas=mycanvas
    
    print('mycanvas',canvas)
    print('path',path)

    def get_mouse_posn(event):
        global topy, topx

        topx, topy = event.x, event.y

    def update_sel_rect(event):
        global rect_id
        global topy, topx, botx, boty

        botx, boty = event.x, event.y
        canvas.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.


    # img = ImageTk.PhotoImage(Image.open(path))
    # canvas = tk.Canvas(root, width=img.width(), height=img.height(),
    #                 borderwidth=0, highlightthickness=0)
    # canvas.pack(expand=True)
    # canvas.img = img  # Keep reference in case this code is put into a function.
    # canvas.create_image(0, 0, image=img, anchor=tk.NW)

    #Create selection rectangle (invisible since corner points are equal).
    rect_id = canvas.create_rectangle(topx, topy, topx, topy,
                                    width=2, outline='green')

    canvas.bind('<Button-1>', get_mouse_posn)
    canvas.bind('<B1-Motion>', update_sel_rect)

    print('rect_id',rect_id)

#######################################################################################
# ComboBox creation

#######################################################################################
# Region Selection

class ExampleApp(tk.Tk):
    def __init__(self,path):
        tk.Tk.__init__(self)

        self.path=path

        # print("Path=",path)

        img = ImageTk.PhotoImage(Image.open(path))
        self.canvas = tk.Canvas(self, width=img.width(), height=img.height(),
                        borderwidth=0, highlightthickness=0, cursor="cross")
        self.canvas.pack(expand=True)
        self.canvas.img = img  # Keep reference in case this code is put into a function.
        self.canvas.create_image(0, 0, image=img, anchor=tk.NW)

        self.x = self.y = 0
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        # self.canvas.bind('<Button-1>', self.get_mouse_posn)
        # self.canvas.bind('<B1-Motion>', self.update_sel_rect)

    def on_button_press(self, event):
        self.x = event.x
        self.y = event.y

    def on_button_release(self, event):
        x0,y0 = (self.x, self.y)
        x1,y1 = (event.x, event.y)
        # global rect_id
        rect_id = self.canvas.create_rectangle(x0,y0,x1,y1, outline="green", width=2)
        # self.canvas.coords(rect_id, x0, y0, x1, y1)  # Update selection rect.
      
    # def get_mouse_posn(event):
        
    #     global topy, topx

    #     topx, topy = event.x, event.y

    # def update_sel_rect(self, event):
    #     global rect_id
    #     global topy, topx, botx, boty

    #     botx, boty = event.x, event.y
    #     self.canvas.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.    

# if __name__ == "__main__":
# app = ExampleApp()
# app.mainloop()
#######################################################################################

