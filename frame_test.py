
from tkinter import *
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
# myapp.master.maxsize(1920, 1024)
myapp.master.geometry("1920x1024+0+0")

# start the program

# master = Tk()  # create root window
myapp.master.title("image2OMR ver:1.0 - Image to OMR reader")
myapp.master.config(bg="gray")
# root.geometry("1360x768+0+0")
# master.geometry("1920x1024+0+0")
# root.resizable(False, False)


frame1 = Frame(myapp.master, width=900, height=640)
frame1.place(x=510,y=192)

frame2=Frame(myapp.master,width=900, height=80, bg="darkgray")
frame2.place(x=510,y=192)
# frame2.config(bg="darkgray")
header2=Label(frame2,text="image2OMR", bg="darkgray", fg="white", font=("Arial-wide",16, "bold")).place(x=10, y=30)

frame3=Frame(frame1, width=500, height=400, bg="darkgray")
frame3.place(x=300,y=150)

footer=Label(myapp.master, text="Copyright © 2023-2048 All rights reserved @NS ", bg="gray", fg="lightgray", font=("Calibri",12, "bold italic")).place(x=1566, y=968)

def layoutDesign():
    frame4 = Frame(myapp.master, width=900, height=640)
    frame4.place(x=510,y=192)


def layoutForm():
    bgc="#FFE4B5"
    fgc="#000000"

    
    # header3=Label(frame1,text="Form Configuration", padx=450, font=("Arial-wide",14, "bold")).place(x=0,y=100)

    btnForm=Button(frame1,text="Forms", width=20, height=2,  bg=bgc, fg=fgc, command=layoutForm).place(x=100,y=200)
    btnTest=Button(frame1,text="Tests", width=20, height=2, command=layoutTest).place(x=100,y=250)
    btnReport=Button(frame1,text="Reports", width=20, height=2, command=layoutReport).place(x=100,y=300)
    
    btnNew=Button(frame3,text="New", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=75,y=75)
    btnModify=Button(frame3,text="Modify", width=20, height=4, bg=bgc, fg=fgc,command=myapp.master.destroy).place(x=275,y=75)
    btnTemplate=Button(frame3,text="Templates", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=75,y=200)
    btnHelp=Button(frame3,text="Help", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=275,y=200)

def layoutTest():
    # bgc="#7289DA"
    bgc="#BDB76B"
    fgc="#000000"

    # header3=Label(frame1,text="Test Configuration", padx=450, fg="red", font=("Arial-wide",14, "bold")).place(x=0,y=100)

    btnForm=Button(frame1,text="Forms", width=20, height=2, command=layoutForm).place(x=100,y=200)
    btnTest=Button(frame1,text="Tests", width=20, height=2,  bg=bgc, fg=fgc, command=layoutTest).place(x=100,y=250)
    btnReport=Button(frame1,text="Reports", width=20, height=2, command=layoutReport).place(x=100,y=300)

    btnNew=Button(frame3,text="New", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=75,y=75)
    btnModify=Button(frame3,text="Configure", width=20, height=4, bg=bgc, fg=fgc,command=myapp.master.destroy).place(x=275,y=75)
    btnEvaluate=Button(frame3,text="Evaluate", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=75,y=200)
    btnHelp=Button(frame3,text="Modify", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=275,y=200)

def layoutReport():
    bgc="#4682B4"
    fgc="#ffffff"

    # header3=Label(frame1,text="Report Generation", padx=450, fg="#4682B4", font=("Arial-wide",14, "bold")).place(x=0,y=100)

    btnForm=Button(frame1,text="Forms", width=20, height=2, command=layoutForm).place(x=100,y=200)
    btnTest=Button(frame1,text="Tests", width=20, height=2, command=layoutTest).place(x=100,y=250)
    btnReport=Button(frame1,text="Reports", width=20, height=2, bg=bgc, fg=fgc, command=layoutReport).place(x=100,y=300)

    btnNew=Button(frame3,text="New", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=75,y=75)
    btnModify=Button(frame3,text="Modify", width=20, height=4, bg=bgc, fg=fgc,command=myapp.master.destroy).place(x=275,y=75)
    btnEvaluate=Button(frame3,text="Evaluate", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=75,y=200)
    btnHelp=Button(frame3,text="Help", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=275,y=200)

# btnForm=Button(frame1,text="Forms", width=20, height=2, command=layoutForm).place(x=100,y=200)

btnForm=Button(frame1,text="Forms", width=20, height=2,  bg="#FFE4B5", fg="#000000", command=layoutForm).place(x=100,y=200)
btnTest=Button(frame1,text="Tests", width=20, height=2, command=layoutTest).place(x=100,y=250)
btnReport=Button(frame1,text="Reports", width=20, height=2, command=layoutReport).place(x=100,y=300)

btnHelp=Button(frame1,text="Help", width=20, height=2).place(x=100,y=350)
btnClose=Button(frame1,text="Exit", width=20, height=2, command=myapp.master.destroy).place(x=100,y=400)


# default
bgc="#FFE4B5"
fgc="#000000"

# header3=Label(frame1,text="Form Configuration", padx=450, font=("Arial-wide",14, "bold")).place(x=0,y=100)

btnNew=Button(frame3,text="New", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=75,y=75)
btnModify=Button(frame3,text="Modify", width=20, height=4, bg=bgc, fg=fgc,command=myapp.master.destroy).place(x=275,y=75)
btnTemplate=Button(frame3,text="Templates", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=75,y=200)
btnHelp=Button(frame3,text="Help", width=20, height=4, bg=bgc, fg=fgc, command=myapp.master.destroy).place(x=275,y=200)



myapp.mainloop()