import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

import interface.canvas.DrawingCanvas as DC
from . import Channel
from .Channels_list import *


class MasterPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.place(height=500, width=700)
        self.canvas = DC.DrawingCanvas(self)


        self.Play_but = ttk.Button(self, text='Play', command=lambda :self.master_play())
        self.Play_but.pack()

        self.Play_stop = ttk.Button(self, text='Stop', command=lambda: self.master_stop_play())
        self.Play_stop.pack()

        self.Add_channel = ttk.Button(self, text='Add_channel', command=lambda: [Channel_list.append(Channel.Channel(self)),Channel_list[-1].insert()])
        self.Add_channel.pack()
        self.bttn_clicks=[] #for creating new channel


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




