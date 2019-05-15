import numpy as np
import pyaudio
from global_.gl_vectors import *
from drawing import paint
import global_.setup as setup


p = pyaudio.PyAudio()

def waveshape_APP():

    paint.paint_master()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,channels=1,rate=Setup.fs,output=True)

    while 1:
        #setup.Setup.freq = setup.Setup.freq - 0.5
        samples = np.float32(paint.reading())
        stream.write(samples)

    stream.stop_stream()
    stream.close()
    p.terminate()

