import tkinter as tk
import drawing.DrawingCanvas as DC
import sound.sound_ as sound
import threading




class Canvas:
    def __init__(self, master = None):
        self.canvas = DC.DrawingCanvas().drawing_area
    def show(self):
        self.canvas.pack()
    def hide(self):
        self.canvas.pack_forget()


class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.canvas = Canvas(self)

        self.Show_but = tk.Button(self,text='Show', command = lambda: self.add_canvas())
        self.Show_but.pack()

        self.Hide_but = tk.Button(self, text='Hide', command=lambda: self.hide_canvas())
        self.Hide_but.pack()

        self.Play_but = tk.Button(self, text='Play', command=lambda :sound.SoundApp().switchon())
        self.Play_but.pack()

        self.Play_stop = tk.Button(self, text='Stop', command=lambda: sound.SoundApp().switchoff())
        self.Play_stop.pack()



    def add_canvas(self):
        self.canvas.show()
    def hide_canvas(self):
        self.canvas.hide()


    def kill(self):
        root.destroy()




#root = tk.Tk()
#root.geometry('300x300')

#a = StartPage(root)
#root.mainloop()