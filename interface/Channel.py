
from tkinter import ttk


from sound.sound_ import SoundApp
from .inside_classes.ChannelLabel import Lab
from .inside_classes.ChannelScale import ChannelScale
from .inside_classes.ChannelButt import Butt

from .inside_classes.PopupWindow import PopupWindow


from .Channels_list import Channel_list


class Channel(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.HideShowButt=Butt(self,'Hide',self.hide_popup_window)
        self.PlayStopButt = Butt(self,'Play',self.play)  # przerobić na jedną klasę przycisk
        self.FreqLabel=Lab(self,'''Modulation Frequency''')
        self.ModulationFreqSlider = ChannelScale(self, "horizontal", 50, 50, 500)
        self.ModDepthLabel = Lab(self, '''Modulation Depth''')
        self.ModulationDepthSlider=ChannelScale(self,"horizontal",0,0,1)
        self.VolumeSlider = ChannelScale(self,"vertical",1,1,0)
        self.VolLabel = Lab(self, '''Volume''')
        self.ChannelLabel = Lab(self,'''Channel''')
        self.PopupWindow=PopupWindow(self)
        self.Canvas = self.PopupWindow.canvas

        self.Sound = SoundApp(self.Canvas,self)

        # what happens if someone closes popup window
        self.PopupWindow.protocol("WM_DELETE_WINDOW", self.exiting_window)




        self.bttn_clicks=0 #clicks of button "Add channel" in MasterPage


    def insert(self):

        self.update_count()

        if self.bttn_clicks == 1:
            self.place(relx=0.067, rely=0.4, height=400, width=200)
        elif self.bttn_clicks == 2:
            self.place(relx=0.351, rely=0.4, height=400, width=200)
        elif self.bttn_clicks == 3:
            self.place(relx=0.638, rely=0.4, height=400, width=200)

    def hide_popup_window(self):
        self.PopupWindow.withdraw()
        self.HideShowButt.configure(text="Show")
        self.HideShowButt.configure(command=lambda: self.show_popup_window())

    def show_popup_window(self):
        self.PopupWindow.deiconify()
        self.HideShowButt.configure(text="Hide")
        self.HideShowButt.configure(command=lambda: self.hide_popup_window())

    def exiting_window(self): #what happens if someone close popup window
        self.PopupWindow.iconify()
        self.hide_popup_window()


    def play(self):
        self.Sound.switchon()
        self.PlayStopButt.configure(text="Stop",command = lambda: self.stop_play())
    def stop_play(self):
        self.Sound.switchoff()
        self.PlayStopButt.configure(text="Play", command=lambda: self.play())

    def update_count(self):
        self.bttn_clicks += 1


