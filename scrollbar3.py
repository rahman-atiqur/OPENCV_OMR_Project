import cv2
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image


win=Tk()
win.geometry("1400x1754")
win.title("MyScrollBar")

wraper1=LabelFrame(win)
wraper2=LabelFrame(win)

mycanvas=Canvas(wraper1)
mycanvas.pack(side=LEFT,fill="both", expand="yes")

yscrollbar=ttk.Scrollbar(wraper1, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
 
myframe=Frame(mycanvas)
mycanvas.create_window((0,0), window=myframe, anchor="nw")

wraper1.pack(fill='both', expand='yes', padx=10, pady=10)
# wraper2.pack(fill='both', expand='yes', padx=10, pady=10)


img = Image.open("OMR_60.jpg")
photo = ImageTk.PhotoImage(img)
label = Label(myframe, image=photo, bg='green')
label.img = photo
label.pack(expand=True, fill=BOTH)
    
# label.img = photo
# label.pack(expand=True, fill=BOTH)

# for i in range(50):
#     Button(myframe, text="My Button"+str(i)).pack()

# win.geometry("1400x1754")
# win.resizable(False,False)
# win.geometry("500x500")
# win.resizable(False,False)
# win.title("MyScrollBar")



#############################

# prevX,prevY=-1,-1
# def printCoordinate(event, x, y, flags, params):
#     global prevX,prevY,img
#     # if event==cv2.EVENT_LBUTTONDOWN:
    
#     if event==cv2.EVENT_LBUTTONDOWN:
#         # cv2.circle(img,(x,y),3,(255,255,255),-1)
#         # strXY='('+str(x)+','+str(y)+')'
#         # font=cv2.FONT_HERSHEY_PLAIN
#         # cv2.putText(img,strXY,(x+10,y-10),font,1,(255,255,255))
#         if prevX==-1 and prevY==-1:
#             prevX,prevY=x,y
#         else:
#             cv2.rectangle(img,(prevX,prevY),(x,y),(0,255,0),2)
#             prevX,prevY=-1,-1

#         # cv2.imshow("Grid selection",img)
#         # img = Image.open("OMR_60.jpg")
#         # photo = ImageTk.PhotoImage(img)
#         label = Label(myframe, image=photo, bg='green')
#         label.img = photo
#         label.pack(expand=True, fill=BOTH)
    

# # img = np.zeros((800,800,3),dtype=np.uint8)

# # img=cv2.imread('OMR_60.jpg')
# # img=cv2.resize(img,(1241,1754))
# # cv2.imshow("Grid selection",img)
# img = Image.open("OMR_60.jpg")
# photo = ImageTk.PhotoImage(img)
# label = Label(myframe, image=photo, bg='green')
# label.img = photo
# label.pack(expand=True, fill=BOTH)

# cv2.setMouseCallback("image", printCoordinate)

# cv2.waitKey()
# cv2.destroyAllWindows()
win.mainloop()

