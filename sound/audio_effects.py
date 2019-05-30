import numpy as np


def count(f):
    def wrapped(**kwargs):
        wrapped.calls += 1
        return f(**kwargs)
    wrapped.calls = 0
    return wrapped


class ChangeAudio:
    def __init__(self):
        self.keyword_functions = {
            'volume': self.volume,
            'fm' : self.fm
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


    def fm(self):
        pass