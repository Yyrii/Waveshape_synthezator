from setup_.setup import Setup
import numpy as np



class ChangeAudio:
    def __init__(self):

        self.keyword_functions = {
            'volume': self.volume,
            'mod_freq':self.mod_freq,
            'lfo':self.lfo
        }

    def set_vec(self, vector):
        self.vector = vector

    def change_audio(self,**kwargs):
        for key, val in kwargs.items():
            self.keyword_functions[key](val)

    def return_vec(self):
        return self.vector

    def volume(self, vol):
        self.vector = [vol*el for el in self.vector]

    def mod_freq(self,freq):
        output = []
        t = np.arange(0, 1, 1 /Setup.fs)

        for i in range(len(t)):
            output.append(1 * np.sin(2 * t[i] * np.pi * freq))

       #self.sin=output
        self.vector = [np.multiply(self.vector, 3 + el) for el in output]

    def lfo(self,sin):
        #self.vector=[self.vector*el for el in sin]
        output = []

        t = np.arange(0, 0.2, 1 / 48000)
        for i in range(len(t)):
            output.append(float(1) * np.sin(2 * t[i] * np.pi * 100))

        #self.vector = self.vector * output
        print(output)
        self.vector = [np.multiply(self.vector,el) for el in output]


