from interface.canvas.DrawingCanvas import *
from sound.wave_operations import wave_operations as w_o


def paint_master():
    root = tk.Tk()
    paint_app = DrawingCanvas()
    root.mainloop()


def reading():
    result =  w_o.freq_adapter(Setup.freq,w_o.fixing_vector(vector_y,lines),Setup.fs)
    for i in range(3): # expanding vector to avoid buzzing
        result += result
    return result