import tkinter as tk
import drawing.DrawingCanvas as DC



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Bank system")
        self.label.pack(pady=10, padx=10)
        controller.geometry("800x600")

        self.Play = tk.Button(self, text="Play",
                                   command=lambda: None)
        #self.Play.place(relx=0.079, rely=0.685, height=54, width=97)
        self.Play.pack()

        self.Canvas_area = CanvasArea().canvas_area


class CanvasArea:
    def __init__(self):
        self.canvas_area = DC.DrawingCanvas().drawing_area
        #self.canvas_area.place(relx=0,rely=0.2)

