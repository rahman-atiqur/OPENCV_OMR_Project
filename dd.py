import cv2
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image

topx, topy, botx, boty = 0, 0, 0, 0
path = "OMR_60.jpg"

# win = tk.Tk()
# win.title("Select Area")
# # win.geometry('%sx%s' % (WIDTH, HEIGHT))
# win.geometry("1400x1754")

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

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
app = ExampleApp()
app.mainloop()