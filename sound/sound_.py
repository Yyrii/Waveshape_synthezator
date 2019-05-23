import numpy as np
import pyaudio
from global_.setup import *

from drawing import paint
import global_.setup as setup
import threading
import wave_operations.wave_operations as w_o


class SoundApp:
    def __init__(self, Canvas):
        self.canvas = Canvas
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32, channels=1, rate=Setup.fs, output=True)

    def play(self):
        def start_audio():
            while switch:
                result = w_o.freq_adapter(Setup.freq, self.canvas.return_vec(), Setup.fs)
                for i in range(3):  # expanding vector to avoid buzzing
                    result += result
                samples = np.float32(result)
                self.stream.write(samples)
                if not switch:
                    break


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

