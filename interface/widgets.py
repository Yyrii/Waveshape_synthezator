import tkinter as tk
import drawing.DrawingCanvas as DC
import sound.sound_ as sound
import threading





class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.canvas = DC.DrawingCanvas(self)

        self.Show_but = tk.Button(self, text='Show', command = lambda: self.show_canvas())
        self.Show_but.pack()

        self.Hide_but = tk.Button(self, text='Hide', command=lambda: self.hide_canvas())
        self.Hide_but.pack()

        self.Play_but = tk.Button(self, text='Play', command=lambda :sound.SoundApp(self.canvas).switchon())
        self.Play_but.pack()

        self.Play_stop = tk.Button(self, text='Stop', command=lambda: sound.SoundApp(self.canvas).switchoff())
        self.Play_stop.pack()


    def show_canvas(self):
        self.canvas.show()
    def hide_canvas(self):
        self.canvas.hide()


