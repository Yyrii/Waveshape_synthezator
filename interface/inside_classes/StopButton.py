import tkinter as tk

class StopButt(tk.Button):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack()
        self.configure(text = 'Stop')