import math
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import threading


switch = True


class SoundGenerator:
    signal = []

    def __init__(self, fs, granule_time, silence_time):
        self.fs = fs
        self.granule_time = granule_time
        self.granule_time /= 1000
        self.silence_time = silence_time

    def adjust_amplitude(self, sig, factor):
        sig = [el * factor for el in sig]
        return sig

    def generate_noise(self, samples_number_):
        noise = np.random.randint(-100, 100, samples_number_)
        noise = [x / 100 for x in noise]
        return noise

    def add_silence(self, sine_, silence_time_ms):
        sine_silence = []
        # silence_time = silence_time_ms/1000
        # silence_time = int(silence_time)
        for el in range(0, len(sine_)):
            sine_silence.append(sine_[el])

        for el in range(0, int((silence_time_ms/1000)*self.fs)):
            sine_silence.append(0)

        return sine_silence

    def calculate_gaussian(self, signal, sigma):
        gauss = []
        sig_len = int(len(signal) / 2)
        for el in range(0, int(len(signal) / 2)):
            gauss.append(math.exp(-1 / 2 * ((el - (sig_len - 1) / 2) / sigma / 2) ** 2))
        for el in range(int(len(signal) / 2) + 1, len(signal) + 1):
            gauss.append(0)
        # self.draw(gauss, 0, 1)
        return gauss

    def add_envelope(self, signal, sigma):
        sine_silence_gaussed = []
        gauss_envelope = self.calculate_gaussian(signal, sigma)
        for el in range(0, int(len(gauss_envelope))):
            sine_silence_gaussed.append(signal[el] * gauss_envelope[el])
        return sine_silence_gaussed

    def update_signal(self, _sig_):
        self.signal = _sig_

    def draw(self):
        plt.plot(self.signal)
        plt.axis([0, int(self.fs * self.granule_time / 2), -1, 1])
        plt.show()


class GranularSynthesizer:
    def __init__(self, gen_, sig):
        self.generator_ = gen_
        self.signal = sig

    def update_gen(self):
        self.signal = 0
        gen = SoundGenerator(fs=44100, granule_time=grain_time_slider.get(), silence_time=silence_time_slider.get())
        gen.samples_number = gen.fs * gen.granule_time
        gen.samples_number = int(gen.samples_number)
        new_noise = gen.generate_noise(gen.samples_number)
        new_noise = gen.adjust_amplitude(new_noise, 0.4)
        new_noise = gen.add_envelope(new_noise, int(gen.granule_time * 800)*sigma_value_slider.get())
        new_noise = gen.add_silence(new_noise, gen.silence_time)
        new_noise_ = gen.adjust_amplitude(new_noise, 1)
        self.generator_ = gen
        gen.signal = new_noise_
        self.generator_.signal = new_noise_
        return new_noise_

    def audio(self):
        def start_audio():
            p = pyaudio.PyAudio()
            stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

            while switch:
                self.signal = self.update_gen()
                samples = np.float32(self.signal)
                stream.write(samples)
                if not switch:
                    break

            stream.stop_stream()
            stream.close()
            p.terminate()

        thread = threading.Thread(target=start_audio)
        thread.start()

    def switch_on(self):
        global switch
        switch = True
        self.audio()

    def switch_off(self):
        global switch
        switch = False

    def change_sig(self):
        # return slider.get()
        pass


generator = SoundGenerator(fs=44100, granule_time=10, silence_time=500)
generator.samples_number = generator.fs * generator.granule_time
generator.samples_number = int(generator.samples_number)
noise = generator.generate_noise(generator.samples_number)
noise = generator.adjust_amplitude(noise, 0.4)
noise = generator.add_envelope(noise, int(generator.granule_time*800))  # second argument is gaussian sigma
noise = generator.add_silence(noise, generator.silence_time)
noise_ = generator.adjust_amplitude(noise, 1)
generator.signal = noise_


synth = GranularSynthesizer(gen_=generator, sig=noise_)

root = tk.Tk()
root.title('Granular')

start_button = tk.Button(root, text="start", command=synth.switch_on)
start_button.pack()

stop_button = tk.Button(root, text="stop", command=synth.switch_off)
stop_button.pack()

draw_button = tk.Button(root, text="draw", command=synth.generator_.draw)
draw_button.pack()

# text_box = tk.Text(root, height=10, width=50)
# text_box.pack()

grain_time_slider = tk.Scale(root, from_=2, to=100, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
grain_time_slider.pack()

silence_time_slider = tk.Scale(root, from_=2, to=500, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
silence_time_slider.pack()

sigma_value_slider = tk.Scale(root, from_=1, to=500, resolution=1, orient=tk.HORIZONTAL, length=300, width=20)
sigma_value_slider.pack()


# def print_slider_value():
#     # text_box.delete(0, tk.END)
#     text_box.insert(tk.INSERT, grain_time_slider.get())


# print_slider_value_button = tk.Button(root, text="slider_value", command=print_slider_value)
# print_slider_value_button.pack()

# load_signal_button = tk.Button(root, text="load_sig", command=make_sound)
# load_signal_button.pack()

tk.mainloop()


# start_audio(sine_silence_gaussed)
# start_audio(sine_silence)
# print(len(sine_silence_gaussed))
# print(len(sine_silence))
# draw(sine)
# draw(sine_silence)
# draw(sine_silence_gaussed)

# https://stackoverflow.com/questions/27050492/how-do-you-create-a-tkinter-gui-stop-button-to-break-an-infinite-loop
# tutaj znajduje sie info jak przerwac nieskonczona petle
