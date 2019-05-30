from tkinter import ttk



class Channel_label(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent)
        #self.place(relx=0.222, rely=0.828, height=19, width=40)
        self.pack()
        self.configure(background="#d9d9d9")
        self.configure(foreground="#000000")
        self.configure(font="TkDefaultFont")
        self.configure(relief="flat")
        self.configure(text='''Channel''')