import tkinter as tk
from PIL import Image, ImageTk

WIDTH, HEIGHT = 900, 900
topx, topy, botx, boty = 0, 0, 0, 0
rect_id = None
path = "OMR_60.jpg"


def get_mouse_posn(event):
    global topy, topx

    topx, topy = event.x, event.y

def update_sel_rect(event):
    global rect_id
    global topy, topx, botx, boty

    botx, boty = event.x, event.y
    canvas.coords(rect_id, topx, topy, botx, boty)  # Update selection rect.

# def on_button_press(self, event):
#     self.x = event.x
#     self.y = event.y

# def on_button_release(self, event):
#     x0,y0 = (self.x, self.y)
#     x1,y1 = (event.x, event.y)

#     self.mycanvas.create_rectangle(x0,y0,x1,y1, outline="green", width=2)

win = tk.Tk()
win.title("Select Area")
# win.geometry('%sx%s' % (WIDTH, HEIGHT))
win.geometry("1400x1754")

win.configure(background='grey')

img = ImageTk.PhotoImage(Image.open(path))
canvas = tk.Canvas(win, width=img.width(), height=img.height(),
                   borderwidth=0, highlightthickness=0)
canvas.pack(expand=True)
canvas.img = img  # Keep reference in case this code is put into a function.
canvas.create_image(0, 0, image=img, anchor=tk.NW)

# Create selection rectangle (invisible since corner points are equal).
rect_id = canvas.create_rectangle(topx, topy, topx, topy,
                                  width=2, outline='green')

canvas.bind('<Button-1>', get_mouse_posn)
canvas.bind('<B1-Motion>', update_sel_rect)

win.mainloop()