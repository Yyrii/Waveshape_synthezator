import numpy as np
from sound.wave_operations.wave_operations import get_sine_index
import time


class ChangeAudio:
    def __init__(self):
        self.index = 0
        self.keyword_functions = {
            'volume': self.volume,
            'fm' : self.fm,
            'modulation':self.modulation
        }

    def set_vec(self, vector):
        self.vector = vector

    def generate_sine(self,freq,amp): #selecting one period of sine
        T=1/float(freq)
        t = np.arange(0, T, 1 / 48000)
        sine=[]
        for i in range(len(t)):
            sine.append(float(amp) * np.sin(2 * t[i] * np.pi * float(freq)))
        return sine

    def set_sine(self,sin):
        self.sine=sin


    def change_audio(self,**kwargs):
        for key, val in kwargs.items():
            self.keyword_functions[key](val)

    def return_vec(self):
        self.index += 1
        return self.vector

    def volume(self, vol):
        self.vector = [vol*el for el in self.vector]

    def modulation(self,mod):
        if mod:
            index = int(("{0:.3f}".format(time.clock())).split('.')[1])  # returns fractial part of time in second
            self.vector = [get_sine_index(mod,index)*el for el in self.vector]

    def fm(self, fm_mod):
        f_carrier = 480
        self.vector = [np.sin(2*np.pi*f_carrier + self.vector[self.index % 100])*fm_mod for el in self.vector]