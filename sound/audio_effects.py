import numpy as np
from sound.wave_operations.wave_operations import get_sine_index
import time


def count(f):
    def wrapped(**kwargs):
        wrapped.calls += 1
        return f(**kwargs)
    wrapped.calls = 0
    return wrapped


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