# importing  all the
# functions defined in py001.py
from logging import root
from operator import mod
from struct import pack
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Progressbar

def new_window03():
    master = Tk()
    master.geometry("200x200")
    label = Label(master,text ="grafics")
    label.pack(pady = 10)
    ########################################
    pb = Progressbar(master,orient='horizontal',mode='determinate',length=280)
    pb.pack(pady=0)
    start_btn = Button(master,text ="Progressbar",command = pb.start)
    stop_btn = Button(master,text ="Progressbar",command = pb.stop)
    start_btn.pack(pady=10)
    stop_btn.pack(pady=20)
    """
    def update_progress_label():
        return f"Current Progress: {pb['value']}%"
    def progress():
        if pb['value'] < 100:
            pb['value'] += 20
            value_label['text'] = update_progress_label()
        else:
            showinfo(message='The progress completed!')
    def stop():
        pb.stop()
        value_label['text'] = update_progress_label()
    value_label = ttk.Label(root, text=update_progress_label()).grid(column=0, row=1, columnspan=2)
    """
    ##################################################
    mainloop()
    


#burada ise calling_func ile func cagirilacak
