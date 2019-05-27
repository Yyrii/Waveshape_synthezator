




class ChangeAudio:
    def __init__(self):

        self.keyword_functions = {
            'volume': self.volume
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
