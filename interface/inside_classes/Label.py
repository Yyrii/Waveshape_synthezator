from tkinter import ttk

class Lab(ttk.Label):
    def __init__(self, parent,text):
        super().__init__(parent)
        self.configure(font="TkDefaultFont")
        self.configure(relief="flat")
        self.configure(text=text)