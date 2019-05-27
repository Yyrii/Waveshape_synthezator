import tkinter as tk

import interface.canvas.DrawingCanvas as DC
from . import Channel
from .Channels_list import *


class MasterPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.canvas = DC.DrawingCanvas(self)


        self.Play_but = tk.Button(self, text='Play', command=lambda :self.master_play())
        self.Play_but.pack()

        self.Play_stop = tk.Button(self, text='Stop', command=lambda: self.master_stop_play())
        self.Play_stop.pack()

        self.Add_channel = tk.Button(self, text='Add_channel', command=lambda: [Channel_list.append(Channel.Channel(self)), Channel_list[-1].place()])
        self.Add_channel.pack()


    def show_canvas(self):
        self.canvas.show()
    def hide_canvas(self):
        self.canvas.hide()

    def master_play(self):
        for el in Channel_list:
            el.play()

    def master_stop_play(self):
        for el in Channel_list:
            el.stop_play()


