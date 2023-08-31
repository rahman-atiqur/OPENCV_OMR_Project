import tkinter as tk
from tkinter import ttk
from tkinter import *


root = Tk()  # create root window
root.title("image2OMR ver:1.0 - Image to OMR reader")
root.config(bg="gray")
# root.geometry("1360x768+0+0")
root.geometry("1920x1024+0+0")
frame1 = Frame(root, width=900, height=640)
frame1.place(x=510,y=192)


root.mainloop()
# cv2.destroyAllWindows()