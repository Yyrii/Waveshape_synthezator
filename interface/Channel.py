import tkinter as tk
from .inside_classes.ChannelScale import ChannelScale
from .inside_classes.ChannelLabel import Channel_label
from .inside_classes.PlayButton import PlayButt
from .inside_classes.StopButton import StopButt
from drawing.DrawingCanvas import DrawingCanvas
from sound.sound_ import SoundApp

class Channel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.MasterScale = ChannelScale(self)
        self.Label = Channel_label(self)
        self.PlayButt = PlayButt(self)
        self.StopButt = StopButt(self)
        self.Canvas = DrawingCanvas(self)
        self.Canvas.show()

        self.Sound = SoundApp(self.Canvas)

        self.PlayButt.configure(command = lambda: self.Sound.switchon())
        self.StopButt.configure(command = lambda: self.Sound.switchoff())

    def place(self):
        self.pack()
    def play(self):
        self.Sound.switchon()
    def stop_play(self):
        self.Sound.switchoff()