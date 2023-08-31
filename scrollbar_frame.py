from tkinter import *


from PIL import ImageTk, Image


ws = Tk()
ws.title('PythonGuides')

img = Image.open("OMR_60.jpg")
photo = ImageTk.PhotoImage(img)

frame4 = Frame(
    ws,
    width=500,
    height=500
    )


frame4.pack(expand=True, fill=BOTH)

canvas=Canvas(
    frame4,
    bg='#4A7A8C',
    width=500,
    height=400,

    scrollregion=(0,0,600,1400)
    )

canvas.img = photo

vertibar=Scrollbar(
    frame4,
    orient=VERTICAL
    )
vertibar.pack(side=RIGHT,fill=Y)
vertibar.config(command=canvas.yview)

horibar=Scrollbar(
    frame4,
    orient=HORIZONTAL
    )
horibar.pack(side=BOTTOM,fill=X)
horibar.config(command=canvas.xview)

canvas.config(width=500,height=500)

canvas.config(
    xscrollcommand=horibar.set, 
    yscrollcommand=vertibar.set
    )
canvas.pack(expand=True,side=LEFT,fill=BOTH)

ws.mainloop()