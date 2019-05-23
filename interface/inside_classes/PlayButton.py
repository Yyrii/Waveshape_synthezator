import tkinter as tk

class PlayButt(tk.Button):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack()
        self.configure(text = 'Play')