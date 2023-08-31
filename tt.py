from tkinter import *
from tkinter import ttk

def comando():
    print(box_value.get())

parent = Tk() #first created window
# ciao=Tk()     #second created window
box_value=StringVar()
# coltbox = ttk.Combobox(parent, textvariable=box_value, state='readonly')
# coltbox["values"] = ["prova","ciao","come","stai"]
# coltbox.current(0)
# coltbox.grid(row=0)
# Button(parent,text="Salva", command=comando, width=20).grid(row=1)

class TableDropDown(ttk.Combobox):
    def __init__(self, parent):
        self.current_table = StringVar() # create variable for table
        ttk.Combobox.__init__(self, parent)#  init widget
        self.config(textvariable = self.current_table, state = "readonly", values = ["Customers", "Pets", "Invoices", "Prices"])
        self.current(0) # index of values for current table
        self.place(x = 50, y = 50, anchor = "w") # place drop down box 
        print(self.current_table.get())
    
parent.mainloop()

# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox

# root = Tk()

# root.geometry("400x400")
# # Length and width window :D

# cmb = ttk.Combobox(root, width="10", values=("prova","ciao","come","stai"))
# # to create checkbox
# # cmb = Combobox

# #now we create simple function to check what user select value from checkbox

# def checkcmbo():

#     if cmb.get() == "prova":
#          messagebox.showinfo("What user choose", "you choose prova")

#     # if user select prova show this message 
#     elif cmb.get() == "ciao":
#         messagebox.showinfo("What user choose", "you choose ciao")

#      # if user select ciao show this message 
#     elif cmb.get() == "come":
#         messagebox.showinfo("What user choose", "you choose come")

#     elif cmb.get() == "stai":
#         messagebox.showinfo("What user choose", "you choose stai")

#     elif cmb.get() == "":
#         messagebox.showinfo("nothing to show!", "you have to be choose something")


# cmb.place(relx="0.1",rely="0.1")

# btn = ttk.Button(root, text="Get Value",command=checkcmbo)
# btn.place(relx="0.5",rely="0.1")

# root.mainloop()