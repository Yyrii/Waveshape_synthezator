from tkinter import ttk


class ChannelScale(ttk.Scale):
    def __init__(self,parent):
        super().__init__(parent)
        #self.place(relx=0.222, rely=0.138, relwidth=0.0, relheight=0.621, width=14, bordermode='ignore')
        self.pack()
        self.configure(orient="vertical")
        self.configure(takefocus="")
        self.configure(from_=0, to=1.0)