import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

import interface.canvas.DrawingCanvas as DC
from . import Channel
from .Channels_list import *


class MasterPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent,width=2000,height=700)
        # self.place(height=500, width=700)
        self.pack()
        # self.canvas = DC.DrawingCanvas(self)

        self.add_bttn_clicks =0


        self.Play_but = ttk.Button(self, text='Play', command=lambda :self.master_play())
        self.Play_but.place(relx=0.133, rely=0.05)

        # self.Play_stop = ttk.Button(self, text='Stop', command=lambda: self.master_stop_play())
        # self.Play_stop.pack()

        self.Add_channel = ttk.Button(self, text='Add Channel')
        self.Add_channel.place(relx=0.133, rely=0.00)
        self.Add_channel.configure(command=lambda: [Channel_list.append(Channel.Channel(self)), self.update_count(),
                                                    Channel_list[-1].insert(self.add_bttn_clicks)])
        self.Master_volume = ttk.Scale(orient="vertical",takefocus="",from_=1, to=0)
        self.Master_volume.set(1)
        self.Master_volume.place(relx=0.3, rely=0.00)

        self.Master_label=ttk.Label(text="Master Volume")
        self.Master_label.place(relx=0.27, rely=0.16)


    def show_canvas(self):
        self.canvas.show()
    def hide_canvas(self):
        self.canvas.hide()

    def master_play(self):
        for el in Channel_list:
            el.play()
        self.Play_but.configure(text="Stop")
        self.Play_but.configure(command=lambda :self.master_stop_play())

    def master_stop_play(self):
        for el in Channel_list:
            el.stop_play()
        self.Play_but.configure(text="Play")
        self.Play_but.configure(command=lambda: self.master_play())

    def update_count(self):
        self.add_bttn_clicks += 1
        if self.add_bttn_clicks>=5:
            self.Add_channel.configure(text="No more channels left")





