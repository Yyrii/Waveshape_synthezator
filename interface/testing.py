from tkinter import *
import drawing.DrawingCanvas as DC

root = Tk()
class AllTkinterWidgets:
    def __init__(self, master):
        #frame = Frame(master, width=500, height=400, bd=1)
        #frame.pack()
        #c = Canvas(frame, bg='black', width=340, height=100)
        c = DC.DrawingCanvas().drawing_area
        c.pack()


# root.option_add('*font', ('verdana', 10, 'bold'))
all = AllTkinterWidgets(root)
root.title('Tkinter Widgets')
root.mainloop()