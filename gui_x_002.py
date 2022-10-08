# importing  all the
# functions defined in py001.py
from calling_func import *
from tkinter import *
from tkinter import ttk


def new_window02():
    master = Tk()
    master.geometry("200x200")
    def openNewWindow():        
        newWindow = Toplevel(master)
        newWindow.title("New Window")
        newWindow.geometry("200x200")
        Label(newWindow,text ="This is a new window").pack()
    label = Label(master,text ="This is the main window")
    label.pack(pady = 10)
    btn = Button(master,text ="Click to open a new window",command = openNewWindow)
    btn.pack(pady = 10)
    mainloop()

#burada ise calling_func ile func cagirilacak
