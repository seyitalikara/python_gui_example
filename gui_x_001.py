# importing  all the
# functions defined in py001.py
from calling_func import *
from tkinter import *
from tkinter import ttk
from gui_x_002 import *
from gui_x_003 import *
from gui_x_004 import *
from gui_x_005 import *


def donothing():
   x = 0
   
def new_tab_01():
   x = 0

def calling_Gui():
#buraya tkinter icin gui yapilacak
    calling_func()
    root = Tk()
    ####################
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new_tab_01)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
    ###########################
    frm = ttk.Frame(root, padding=200)
    frm.grid()
    ttk.Label(frm, text="label2!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    ttk.Label(frm, text="Hello World!").grid(column=0, row=1)
    ttk.Button(frm, text="window1", command=new_window02).grid(column=1, row=1)
    ttk.Label(frm, text="graphics!").grid(column=0, row=2)
    ttk.Button(frm, text="window3", command=new_window03).grid(column=1, row=2)
    ttk.Label(frm, text="vertical!").grid(column=0, row=3)
    ttk.Button(frm, text="window4", command=new_window04).grid(column=1, row=3)
    ttk.Label(frm, text="text!").grid(column=0, row=4)
    ttk.Button(frm, text="window5", command=new_window05).grid(column=1, row=4)

    root.mainloop()
