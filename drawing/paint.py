from drawing.DrawingCanvas import *
import wave_operations.wave_operations as w_o

def paint_master():
    root = Tk()
    paint_app = DrawingCanvas(root)
    root.mainloop()
    result =  w_o.freq_adapter(freq,w_o.fixing_vector(vector_y,lines),fs)
    for i in range(4): # if the vector is too low, there is buzzing problem. This way loops are small (just 4), and sufficient
        result += result
    return result