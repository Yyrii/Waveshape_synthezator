import tkinter as tk
from interface.canvas.DrawingCanvas import DrawingCanvas


class PopupWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.canvas=DrawingCanvas(self)
        self.canvas.show()