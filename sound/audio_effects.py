from setup_.setup import Setup
import numpy as np



class ChangeAudio:
    def __init__(self):

        self.keyword_functions = {
            'volume': self.volume,
            'lfo':self.lfo
        }

    def set_vec(self, vector):
        self.vector = vector

    def generate_sine(self,freq,amp): #setting one period of sine
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
        return self.vector

    def volume(self, vol):
        self.vector = [float(vol)*el for el in self.vector]



    def lfo(self,index):

        self.vector = np.multiply(self.vector,1+self.sine[index])


