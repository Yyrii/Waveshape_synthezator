import tkinter as tk
from tkinter import ttk

from interface.canvas.DrawingCanvas import DrawingCanvas
from sound.sound_ import SoundApp
from .inside_classes.ChannelLabel import Channel_label
from .inside_classes.ChannelScale import ChannelScale
from .inside_classes.PlayButton import PlayButt
from .inside_classes.StopButton import StopButt
from .inside_classes.PopupWindow import PopupWindow


class Channel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.ModulationFreqSlider = ChannelScale(self, "horizontal", 50, 50, 500)
        self.ModulationDepthSlider=ChannelScale(self,"horizontal",0,0,1)
        self.VolumeSlider = ChannelScale(self,"vertical",1,1,0)
        self.Label = Channel_label(self)
        self.PlayButt = PlayButt(self)
        self.StopButt = StopButt(self)
        self.PopupWindow=PopupWindow(self)
        self.Canvas = self.PopupWindow.canvas


        self.Sound = SoundApp(self.Canvas,self)

        self.PlayButt.configure(command = lambda: self.Sound.switchon())
        self.StopButt.configure(command = lambda: self.Sound.switchoff())


    def place(self):
        self.pack()
    def play(self):
        self.Sound.switchon()
    def stop_play(self):
        self.Sound.switchoff()
