from interface.Frames_ import *


class Synthezator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        #waveshape_APP()

        self.frames = {}

        frame = StartPage(container,self)
        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew") #stretching (north, south, east, west)
        waveshape_APP()

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

