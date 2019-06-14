import tkinter as tk
from tkinter import *

from ttkthemes import ThemedTk

import interface.canvas.DrawingCanvas as DC
import sound.sound_ as sound
from interface.inside_classes.ChannelLabel import *
from interface.inside_classes.ChannelScale import *


class Canvas:
    def __init__(self,parent, master=None):
        self.canvas = DC.DrawingCanvas(parent).drawing_area  # tworzy płotno
        # self.canvas.place(relx=0.047, rely=0.1)
        self.canvas.pack()


class New_Window(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.canvas=Canvas(self)




class StartPage(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.place(height=700, width=700)


        self.new_window=[] #vector of popup windows
        self.hide_show_but=[]#vector of show/hide buttons (for popup windows)

        # self.canvas = Canvas(self)

        self.bttn_clicks = 0 #counter of button clicks(for adding new channels)

        #Test buttons for popup window
        self.popup_but = ttk.Button(self, text='New Window', command=lambda: self.popup_window(0))
        self.popup_but.pack()

        self.hide_show_but.append(ttk.Button(self, text='Hide', command=lambda: self.hide_popup_window(0)))
        self.hide_show_but[0].pack()



        self.popup_but2 = ttk.Button(self, text='New Window', command=lambda: self.popup_window(1))
        self.popup_but2.pack()

        self.hide_show_but.append(ttk.Button(self, text='hide', command=lambda: self.hide_popup_window(1)))
        self.hide_show_but[1].pack()




        #------------------------------------------------------------------------------------------

        self.Add_but = ttk.Button(self, text='Add', command=lambda: self.add_block())
        self.Add_but.place(relx=0.067, rely=0.05,height=30, width=46)


        self.Play_but = ttk.Button(self, text='Play')
        self.Play_but.place(relx=0.133, rely=0.05,height=30)
        self.Play_but.bind('<ButtonPress-1>', self.play_start)
        self.Play_but.bind('<ButtonRelease-1>', self.play_stop)

        #Frame 1

        self.Frame1 = ttk.Frame(self)
        # self.Frame1.place(relx=0.067, rely=0.5, height=400, width=200)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.121, rely=0.138, height=19, width=66)
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Modulation''')

        self.TScale1 = ttk.Scale(self.Frame1, from_=0, to=1.0)
        self.TScale1.place(relx=0.121, rely=0.276, relwidth=0.606, relheight=0.0
                           , height=26, bordermode='ignore')
        self.TScale1.configure(takefocus="")
        #Frame 1_1 = volume1
        self.Frame1_1 = ttk.Frame(self.Frame1)
        self.Frame1_1.place(relx=0.727, rely=0.0, relheight=1.0
                               , relwidth=0.273)
        self.Frame1_1.configure(relief='groove')
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(relief="groove")

        self.TScale4 = ttk.Scale(self.Frame1_1, from_=0, to=1.0)
        self.TScale4.place(relx=0.222, rely=0.138, relwidth=0.0, relheight=0.621
                           , width=14, bordermode='ignore')
        self.TScale4.configure(orient="vertical")
        self.TScale4.configure(length="90")
        self.TScale4.configure(takefocus="")

        self.TLabel3 = ttk.Label(self.Frame1_1)
        self.TLabel3.place(relx=0.222, rely=0.828, height=19, width=21)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''Vol''')

        #Frame 2

        self.Frame2 = ttk.Frame(self)
        # self.Frame2.place(relx=0.333, rely=0.5, height=400, width=200)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.Frame2)
        self.TLabel1.place(relx=0.121, rely=0.138, height=19, width=66)
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Modulation''')

        self.TScale2 = ttk.Scale(self.Frame2, from_=0, to=1.0)
        self.TScale2.place(relx=0.171, rely=0.276, relwidth=0.571, relheight=0.0
                           , height=26, bordermode='ignore')
        self.TScale2.configure(takefocus="")
        #Frame 2_1

        self.Frame2_1 = ttk.Frame(self.Frame2)
        self.Frame2_1.place(relx=0.743, rely=0.0, relheight=1.0
                               , relwidth=0.257)
        self.Frame2_1.configure(relief='groove')
        self.Frame2_1.configure(borderwidth="2")
        self.Frame2_1.configure(relief="groove")
        #add8e6


        self.TScale4_1 = ttk.Scale(self.Frame2_1, from_=0, to=1.0)
        self.TScale4_1.place(relx=0.222, rely=0.138, relwidth=0.0, relheight=0.621
                           , width=14, bordermode='ignore')
        self.TScale4_1.configure(orient="vertical")
        self.TScale4_1.configure(takefocus="")

        self.TLabel3_3 = ttk.Label(self.Frame2_1)
        self.TLabel3_3.place(relx=0.222, rely=0.828, height=19, width=21)
        self.TLabel3_3.configure(background="#d9d9d9")
        self.TLabel3_3.configure(foreground="#000000")
        self.TLabel3_3.configure(font="TkDefaultFont")
        self.TLabel3_3.configure(relief="flat")
        self.TLabel3_3.configure(text='''Vol''')

        #Frame 3

        self.Frame3 = ttk.Frame(self)
        # self.Frame3.place(relx=0.617, rely=0.5, height=400, width=200)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.Frame3)
        self.TLabel1.place(relx=0.121, rely=0.138, height=19, width=66)
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Modulation''')

        self.TScale3 = ttk.Scale(self.Frame3, from_=0, to=1.0)
        self.TScale3.place(relx=0.114, rely=0.276, relwidth=0.571, relheight=0.0
                           , height=26, bordermode='ignore')
        self.TScale3.configure(takefocus="")
        #Frame 3_1

        self.Frame3_1 = ttk.Frame(self.Frame3)
        self.Frame3_1.place(relx=0.743, rely=0.0, relheight=1.0
                               , relwidth=0.257)
        self.Frame3_1.configure(relief='groove')
        self.Frame3_1.configure(borderwidth="2")
        self.Frame3_1.configure(relief="groove")

        self.TScale4_2 = ttk.Scale(self.Frame3_1, from_=0, to=1.0)
        self.TScale4_2.place(relx=0.222, rely=0.138, relwidth=0.0, relheight=0.621
                           , width=14, bordermode='ignore')
        self.TScale4_2.configure(orient="vertical")
        self.TScale4_2.configure(takefocus="")

        self.TLabel3_4 = ttk.Label(self.Frame3_1)
        self.TLabel3_4.place(relx=0.222, rely=0.828, height=19, width=21)
        self.TLabel3_4.configure(background="#d9d9d9")
        self.TLabel3_4.configure(foreground="#000000")
        self.TLabel3_4.configure(font="TkDefaultFont")
        self.TLabel3_4.configure(relief="flat")
        self.TLabel3_4.configure(text='''Vol''')

        #Master volume

        self.Frame4 = ttk.Frame(self)
        self.Frame4.place(relx=0.915, rely=0.7, height=200, width=60)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")

        self.Master_Scale = ChannelScale(self.Frame4)

        self.Master_label = Channel_label(self.Frame4)



    running = False

    def update_count(self):
        self.bttn_clicks += 1
    #Adding channel
    def add_block(self):
        self.update_count()
        # frame_x = "Frame" + str(self.bttn_clicks)
        if self.bttn_clicks==1:
            self.Frame1.place(relx=0.067, rely=0.7, height=200, width=200)
        elif self.bttn_clicks==2:
            self.Frame2.place(relx=0.351, rely=0.7, height=200, width=200)
        elif self.bttn_clicks == 3:
            self.Frame3.place(relx=0.638, rely=0.7, height=200, width=200)#284
    def popup_window(self,nr):

        self.new_window.append(New_Window(self))
    def hide_popup_window(self,nr):
        self.new_window[nr].withdraw()
        self.hide_show_but[nr].configure(text="Show")
        self.hide_show_but[nr].configure(command=lambda: self.show_popup_window(nr))
    def show_popup_window(self,nr):
        self.new_window[nr].deiconify()
        self.hide_show_but[nr].configure(text="Hide")
        self.hide_show_but[nr].configure(command=lambda: self.hide_popup_window(nr))









    def play_start(self, event):
        global running
        running = True
        sound.waveshape_APP()

    def play_stop(self, event):
        global running
        running = False

    def add_canvas(self):
        self.canvas.show()

    def hide_canvas(self):
        self.canvas.hide()


# root = tk.Tk()
#
# a = StartPage(root)
# root.mainloop()

window = ThemedTk(theme="equilux")
a = StartPage(window)
# ttk.Button(window, text="Quit", command=DC.drawing_area).pack()
window.mainloop()



