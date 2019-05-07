from drawing.DrawingCanvas import *
import wave_operations.wave_operations as w_o

def paint_master():
    root = Tk()
    paint_app = DrawingCanvas(root)
    root.mainloop()

def reading():
    result =  w_o.freq_adapter(Setup.freq,w_o.fixing_vector(vector_y,lines),Setup.fs)
    for i in range(3): # if the vector is too low, there is buzzing problem. This way loops are small (just 4), and sufficient
        result += result
    return result