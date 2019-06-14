import threading
import numpy as np
import pyaudio
from setup_.setup import *
from sound.wave_operations import wave_operations as w_o
from sound.audio_effects import ChangeAudio


class SoundApp:
    def __init__(self, Canvas,Channel):
        self.canvas = Canvas
        self.channel=Channel
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32, channels=2, rate=Setup.fs, output=True)
        self.AudioChanger = ChangeAudio()
        self.ChannelScale = ChannelScale
        #self.freq = Setup.freq -> czytanie częstotliwości

    def play(self):
        def start_audio():
            while switch:
                mod_freq=self.channel.ModulationFreqSlider.get_position()
                sin=self.AudioChanger.generate_sine(mod_freq,self.channel.ModulationDepthSlider.get_position())
                self.AudioChanger.set_sine(sin)
                canvas_samples = w_o.freq_adapter(Setup.freq, self.canvas.return_vec(), Setup.fs)
                # zrobić funkcję zwracającą sinusa w audio_effects
                for i in range(3):  # expanding vector to avoid buzzing
                    canvas_samples += canvas_samples
                for i in range(len(self.AudioChanger.sine)):

                self.AudioChanger.set_vec(canvas_samples)
                self.AudioChanger.change_audio(volume=1-self.ChannelScale.get(), modulation=0)
                audio = self.AudioChanger.return_vec()

                for i in range(4):  # expanding vector to avoid buzzing
                    audio += audio
                samples = np.float32(audio)
                self.stream.write(np.ravel(np.column_stack((samples, samples/2)))) # stereo, L R
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

