import cv2
import numpy as np
import tkinter as tk
import utils


from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from scipy.ndimage import interpolation as inter

from PIL import ImageTk, Image

def homePage(root):

    # root = Tk()  # create root window
    # root.title("image2OMR ver:1.0 - Image to OMR reader")
    # root.config(bg="gray")
    # # root.geometry("1360x768+0+0")
    # root.geometry("1920x1024+0+0")
    # # root.resizable(False, False)


    frame1 = Frame(root, width=900, height=640)
    frame1.place(x=510,y=192)

    frame2=Frame(root,width=900, height=80, bg="darkgray")
    frame2.place(x=510,y=192)
    # frame2.config(bg="darkgray")
    header2=Label(frame2,text="image2OMR", bg="darkgray", fg="white", font=("Arial-wide",16, "bold")).place(x=10, y=30)

    frame3=Frame(frame1, width=500, height=400, bg="darkgray")
    frame3.place(x=300,y=150)

    footer=Label(root, text=" Copyright © 2023-2048 All rights reserved @NS ", bg="gray", fg="lightgray", font=("Calibri",12, "italic")).place(x=1566, y=968)
    
    myframe=''

    def layoutDesign():
        global myframe
        frame41 = Frame(root, width=1920, height=1024, bg="gray")
        frame41.place(x=0,y=0)
        frame4 = Frame(frame41, width=1400, height=1024, bg="gray")
        frame4.place(x=0,y=0)
        frame5 = Frame(frame41, width=520, height=1024)
        frame5.place(x=1401,y=0)

        btnHome=Button(frame5, text="Home", width=20, height=2, command= frame41.destroy).place(x=100,y=200)
        btnQuit=Button(frame5, text="Quit", width=20, height=2, command= root.destroy).place(x=100,y=250)

        footer=Label(root, text=" Copyright © 2023-2048 All rights reserved @NS ", fg="gray", font=("Calibri",12, "italic")).place(x=1566, y=968)
        
        ###############################################

        ###############################
        # displaying image in a vertical scrollbar

        wraper1=LabelFrame(frame4)

        # mycanvas=Canvas(wraper1)
        mycanvas=Canvas(wraper1, width=1300, height=1024)
        mycanvas.pack(side=LEFT, fill="both", expand="yes")

        yscrollbar=Scrollbar(wraper1, orient="vertical", command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill="y")

        mycanvas.configure(yscrollcommand=yscrollbar.set)

        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        
        myframe=Frame(mycanvas)
        mycanvas.create_window((0,0), window=myframe, anchor="nw")

        wraper1.pack(fill='both', expand='yes', padx=30,pady=20)
        # wraper1.pack(fill='both', expand='yes', padx=10, pady=10)

        # ##################################################################
        # image_path="OMR_100_new_skewed.jpg"
        
        # # image_path="OMR_60s.jpg"
        # ##################################################################

        # # Resizing by A4
        # widthImg=1241
        # heightImg=1754

        # # Resizing by Letter
        # # widthImg=1275
        # # heightImg=1650
        
        # im=cv2.imread(image_path)
        # im=cv2.resize(im,(widthImg,heightImg))
        # cv2.imwrite('resized.jpg',im)
        # # image_path=cv2.imshow('resized.jpg',im)
        # image_path="resized.jpg"
        # ##################################################################

        # img = Image.open(image_path)
        # photo = ImageTk.PhotoImage(img)
        # label = Label(myframe, image=photo, bg='green')
            
        # label.img = photo
        # label.pack(expand=True, fill=BOTH)

        # return myframe

    def layoutForm():
        bgc="#FFE4B5"
        fgc="#000000"

        
        # header3=Label(frame1,text="Form Configuration", padx=450, font=("Arial-wide",14, "bold")).place(x=0,y=100)

        btnForm=Button(frame1,text="Forms", width=20, height=2,  bg=bgc, fg=fgc, command=layoutForm).place(x=100,y=200)
        btnTest=Button(frame1,text="Tests", width=20, height=2, command=layoutTest).place(x=100,y=250)
        btnReport=Button(frame1,text="Reports", width=20, height=2, command=layoutReport).place(x=100,y=300)
        
        btnNew=Button(frame3,text="New", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=75,y=75)
        btnModify=Button(frame3,text="Modify", width=20, height=4, bg=bgc, fg=fgc,command=root.destroy).place(x=275,y=75)
        btnTemplate=Button(frame3,text="Templates", width=20, height=4, bg=bgc, fg=fgc, command=layoutDesign).place(x=75,y=200)
        btnHelp=Button(frame3,text="Help", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=275,y=200)

    def layoutTest():
        # bgc="#7289DA"
        bgc="#BDB76B"
        fgc="#000000"

        # header3=Label(frame1,text="Test Configuration", padx=450, fg="red", font=("Arial-wide",14, "bold")).place(x=0,y=100)

        btnForm=Button(frame1,text="Forms", width=20, height=2, command=layoutForm).place(x=100,y=200)
        btnTest=Button(frame1,text="Tests", width=20, height=2,  bg=bgc, fg=fgc, command=layoutTest).place(x=100,y=250)
        btnReport=Button(frame1,text="Reports", width=20, height=2, command=layoutReport).place(x=100,y=300)

        btnNew=Button(frame3,text="New", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=75,y=75)
        btnModify=Button(frame3,text="Configure", width=20, height=4, bg=bgc, fg=fgc,command=root.destroy).place(x=275,y=75)
        btnEvaluate=Button(frame3,text="Evaluate", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=75,y=200)
        btnHelp=Button(frame3,text="Modify", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=275,y=200)

    def layoutReport():
        bgc="#4682B4"
        fgc="#ffffff"

        # header3=Label(frame1,text="Report Generation", padx=450, fg="#4682B4", font=("Arial-wide",14, "bold")).place(x=0,y=100)

        btnForm=Button(frame1,text="Forms", width=20, height=2, command=layoutForm).place(x=100,y=200)
        btnTest=Button(frame1,text="Tests", width=20, height=2, command=layoutTest).place(x=100,y=250)
        btnReport=Button(frame1,text="Reports", width=20, height=2, bg=bgc, fg=fgc, command=layoutReport).place(x=100,y=300)

        btnNew=Button(frame3,text="New", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=75,y=75)
        btnModify=Button(frame3,text="Modify", width=20, height=4, bg=bgc, fg=fgc,command=root.destroy).place(x=275,y=75)
        btnEvaluate=Button(frame3,text="Evaluate", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=75,y=200)
        btnHelp=Button(frame3,text="Help", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=275,y=200)



    # btnForm=Button(frame1,text="Forms", width=20, height=2, command=layoutForm).place(x=100,y=200)

    btnForm=Button(frame1,text="Forms", width=20, height=2,  bg="#FFE4B5", fg="#000000", command=layoutForm).place(x=100,y=200)
    btnTest=Button(frame1,text="Tests", width=20, height=2, command=layoutTest).place(x=100,y=250)
    btnReport=Button(frame1,text="Reports", width=20, height=2, command=layoutReport).place(x=100,y=300)

    btnHelp=Button(frame1,text="Help", width=20, height=2).place(x=100,y=350)
    btnClose=Button(frame1,text="Exit", width=20, height=2, command=root.destroy).place(x=100,y=400)


    # default
    bgc="#FFE4B5"
    fgc="#000000"

    # header3=Label(frame1,text="Form Configuration", padx=450, font=("Arial-wide",14, "bold")).place(x=0,y=100)

    btnNew=Button(frame3,text="New", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=75,y=75)
    btnModify=Button(frame3,text="Modify", width=20, height=4, bg=bgc, fg=fgc,command=root.destroy).place(x=275,y=75)
    btnTemplate=Button(frame3,text="Templates", width=20, height=4, bg=bgc, fg=fgc, command=layoutDesign).place(x=75,y=200)
    btnHelp=Button(frame3,text="Help", width=20, height=4, bg=bgc, fg=fgc, command=root.destroy).place(x=275,y=200)


    # myframe=myframe
    return myframe  