# importing  all the
# functions defined in py001.py
from logging import root
from operator import mod
from struct import pack
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Progressbar

def new_window04():
    master = Tk()
    master.geometry("400x500")
    master.grid()
    label = Label(master,text ="progress sistemi")
    label.grid(column=0, row=0)
    ########################################
    pb = Progressbar(master,orient='vertical',mode='determinate',length=140)
    pb.grid(column=0, row=1)
    label_upd = Label(master, text="!")
    label_upd.grid(column=0, row=2)
    def start_sys():
        pb.start()   
        label_upd.config(text= "sistem çalışıyor!")
    
    def stop_sys():        
        pb.stop()
        label_upd.config(text= "sistem durdu!")

    start_btn = Button(master,text ="start",command = start_sys)
    stop_btn = Button(master,text ="stop",command = stop_sys)
    start_btn.grid(column=0, row=3)
    stop_btn.grid(column=0, row=4)
    ##################################################
    Label(master, text="quit!").grid(column=0, row=5)
    Button(master, text="Quit", command=master.destroy).grid(column=0, row=6)
    mainloop()
    