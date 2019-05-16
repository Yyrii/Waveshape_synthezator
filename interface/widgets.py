import tkinter as tk
import drawing.DrawingCanvas as DC
import sound.sound_ as sound




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

        # play button
        self.Show_but = tk.Button(self,text='Show', command = lambda: self.add_canvas())
        self.Show_but.pack()

        self.Hide_but = tk.Button(self, text='Hide', command=lambda: self.hide_canvas())
        self.Hide_but.pack()

        self.Play_but = tk.Button(self, text='Play', command=lambda: None)
        self.Play_but.pack()

        self.Play2_but = tk.Button(self, text='Play2', command=lambda: None)
        self.Play2_but.pack()

        self.button = tk.Button(self, text="forward")
        self.button.pack()
        self.button.bind('<ButtonPress-1>', self.start_motor)
        self.button.bind('<ButtonRelease-1>', self.stop_motor)

    running = False

    def start_motor(self,event):
        global running
        running = True
        sound.waveshape_APP()

    def stop_motor(self,event):
        global running
        running = False



    def add_canvas(self):
        self.canvas.show()
    def hide_canvas(self):
        self.canvas.hide()




root = tk.Tk()

a = StartPage(root)
root.mainloop()