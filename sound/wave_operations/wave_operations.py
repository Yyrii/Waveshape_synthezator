import numpy as np
import matplotlib.pyplot as plt
import setup_.setup as setup


def get_sine_index(freq,index):  # getting specified index of sine
    return np.sin(np.pi * freq*index*(1/1000)*2.)

# def index_sine(freq,index): #setting one period of sine
#     T=1/float(freq)
#     t = np.arange(0, T, 1 / setup.Setup.fs)
#
#     sine = [np.sin(2 * time * np.pi * float(freq)) for time in t]
#     return sine[index]


def freq_adapter(freq, input_v, fs):
    expected_width = int(fs / freq)          # how wide will the output vector be
    window = int(len(input_v) / expected_width)

    output_v = []
    offset = 0
    for i in range(expected_width):
        output_v.append(np.mean(input_v[ offset+i*window : offset+(i+1)*window]))
    return output_v
# x=[]
# for i in range(1000):
#     x.append(get_sine_index(10,i))
# plt.plot(x)
# plt.show()