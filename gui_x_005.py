# importing  all the
# functions defined in py001.py
from cgitb import text
from logging import root
from operator import mod
from struct import pack
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Progressbar
from turtle import home
from gui_x_004 import *

def new_window05():
    master = Tk()
    master.geometry("500x500")
    master.grid()
    label = Label(master,text ="text ile note")
    label.grid(column=0, row=0)
    ########################################
    T = Text(master, height = 3, width = 52)
    T.grid(column=0, row=1)
    # Create label
    l = Label(master, text = "Fact of the Day")
    l.config(font =("Courier", 14))
    l.grid(column=0, row=2)
    Fact = """A man can be arrested in Italy for wearing a skirt in public."""
    
    b2 = Button(master, text = "Exit", command = master.destroy)
    b2.grid(column=0, row=4)
    # Insert The Fact.
    T.insert(END, Fact)
    def Take_input():
        INPUT = inputtxt.get("1.0", "end-1c")
        print(INPUT)
        if(INPUT == "120"):
            Output.insert("1.0", 'Correct'+"\n")
            b1 = Button(master, text = "Next", command=new_window04)    
            b1.grid(column=0, row=3)
        else:
            Output.insert("1.0", "Wrong answer"+"\n")
            l3 = Label(master, text = "you can give up!")
            l3.grid(column=0, row=3)
    l2 = Label(master, text = "What is 24 * 5 ? ")
    inputtxt = Text(master, height = 3,  width = 15, bg = "light yellow")
    Output = Text(master, height = 3, width = 15, bg = "light cyan")
    Display = Button(master, height = 1, width = 15, text ="Show", command = lambda:Take_input())
    l2.grid(column=0, row=5)
    inputtxt.grid(column=0, row=6)
    Display.grid(column=0, row=7)
    Output.grid(column=0, row=8)
    ##################################################
    Label(master, text="quit!").grid(column=0, row=12)
    Button(master, text="Quit", command=master.destroy).grid(column=0, row=13)
    mainloop()
    