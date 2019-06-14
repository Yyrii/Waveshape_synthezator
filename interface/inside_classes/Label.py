from tkinter import ttk



class Lab(ttk.Label):
    def __init__(self, parent,text):
        super().__init__(parent)
        #self.place(relx=0.222, rely=0.828, height=19, width=40)
        self.pack()

        self.configure(font="TkDefaultFont")
        self.configure(relief="flat")
        self.configure(text=text)