import numpy as np
import pyaudio
from global_.gl_vectors import *
from drawing import paint


p = pyaudio.PyAudio()

def waveshape_APP():

    vector_ = paint.paint_master()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,channels=1,rate=fs,output=True)

    while 1:
        samples = np.float32(vector_)
        stream.write(samples)

    stream.stop_stream()
    stream.close()
    p.terminate()

