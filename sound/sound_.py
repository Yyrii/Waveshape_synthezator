import numpy as np
import pyaudio
from global_.gl_vectors import *
from drawing import paint
import global_.setup as setup
import threading


class SoundApp:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32, channels=1, rate=Setup.fs, output=True)

    def play(self):
        def start_audio():
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

            while switch:
                samples = np.float32(paint.reading())
                stream.write(samples)
                if not switch:
                    break

            stream.stop_stream()
            stream.close()
            p.terminate()

        thread = threading.Thread(target=start_audio)
        thread.start()

    def switchon(self):
        global switch
        switch = True
        self.play()

    def switchoff(self):
        global switch
        switch = False


    def __exit__(self, *args):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

