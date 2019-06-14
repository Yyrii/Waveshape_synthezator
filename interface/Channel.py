from tkinter import ttk
from sound.sound_ import SoundApp
from .inside_classes.Label import Lab
from .inside_classes.ChannelScale import ChannelScale
from .inside_classes.ChannelButt import Butt
from .inside_classes.PopupWindow import PopupWindow


class Channel(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.HideShowButt           =Butt(self,'Hide',self.hide_popup_window)
        self.PlayStopButt           =Butt(self,'Play',self.play)  # przerobić na jedną klasę przycisk
        self.FreqLabel              =Lab(self,'''Modulation Frequency''')
        self.ModulationFreqSlider   =ChannelScale(self, orient="horizontal", initial_pos=0, beg_of_scale=0,
                                                  end_of_scale=50)

        self.VolLabel               =Lab(self, '''Volume''')
        self.VolumeSlider           =ChannelScale(self,orient="vertical",initial_pos=1,beg_of_scale=1,
                                                  end_of_scale=0)
        self.PanLabel               =Lab(self, '''Pan''')
        self.Pan                    =ChannelScale(self,orient= "horizontal", initial_pos=0.5,beg_of_scale= 1,
                                                  end_of_scale= 0)
        self.FreqLabel              =Lab(self, '''Frequency''')
        self.FreqSlider             =ChannelScale(self, orient="horizontal", initial_pos=480,beg_of_scale= 100, end_of_scale= 1200)

        self.Master = parent


    def insert(self,bttn_clicks):
        if bttn_clicks <= 5:
            self.place(relx=0.067+(0.18*(bttn_clicks-1)), rely=0.4, height=400, width=200)
            self.PopupWindow = PopupWindow(self)
            self.PopupWindow.resizable(0, 0)
            self.Canvas = self.PopupWindow.canvas
            self.Sound = SoundApp(self.Canvas, self)
            # what happens if someone closes popup window
            self.PopupWindow.protocol("WM_DELETE_WINDOW", self.exiting_window)

    def hide_popup_window(self):
        self.PopupWindow.withdraw()
        self.HideShowButt.configure(text="Show")
        self.HideShowButt.configure(command=lambda: self.show_popup_window())

    def show_popup_window(self):
        self.PopupWindow.deiconify()
        self.HideShowButt.configure(text="Hide")
        self.HideShowButt.configure(command=lambda: self.hide_popup_window())

    def exiting_window(self): #what happens if someone closes popup window
        self.PopupWindow.iconify()
        self.hide_popup_window()

    def play(self):
        self.Sound.switchon()
        self.PlayStopButt.configure(text="Stop",command = lambda: self.stop_play())
    def stop_play(self):
        self.Sound.switchoff()
        self.PlayStopButt.configure(text="Play", command=lambda: self.play())