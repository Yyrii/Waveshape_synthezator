import tkinter as tk
import drawing.DrawingCanvas as DC
from sound.sound_ import waveshape_APP
from global_.current_state import CurrentState



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Bank system")
        self.label.pack(pady=10, padx=10)
        controller.geometry("508x292+492+193")

        self.Play = tk.Button(self, text="Play",command=lambda: [CurrentState().setTrue()])
        self.Play.pack()

        self.Stop = tk.Button(self, text="Play", command=lambda: CurrentState().setFalse())
        self.Stop.pack()

        self.Hide = tk.Button(self, text="Hide",command=lambda: self.cnv_area.hide())
        self.Hide.pack()

        self.Show = tk.Button(self, text="Show", command=lambda: self.cnv_area.show())
        self.Show.pack()

        self.cnv_area = CanvasArea()
        #self.cnv_area.hide()


class CanvasArea:
    def __init__(self):
        self.cnv_area = DC.DrawingCanvas().drawing_area

    root = tk.Tk()

    def hide(self):
        self.cnv_area.pack_forget()

    def show(self):
        self.cnv_area.pack()
