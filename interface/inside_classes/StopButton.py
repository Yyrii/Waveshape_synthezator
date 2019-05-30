from tkinter import ttk

class StopButt(ttk.Button):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack()
        self.configure(text = 'Stop')