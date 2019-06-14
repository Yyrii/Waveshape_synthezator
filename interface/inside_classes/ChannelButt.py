from tkinter import ttk


class Butt(ttk.Button):
    def __init__(self,parent,text,cmd):
        super().__init__(parent)
        self.configure(text = text,command =cmd)
        self.pack()