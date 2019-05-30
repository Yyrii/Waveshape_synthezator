from tkinter import ttk

class PlayButt(ttk.Button):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack()
        self.configure(text = 'Play')