import numpy as np
import matplotlib.pyplot as plt
import global_.setup as setup




def sine(): #testing draw & sound
    output = []
    for i in range(200):
        output.append(np.sin(i*np.pi/25))
    return output


def freq_adapter(freq, input_v, fs):
    expected_width = int(fs / freq)          # how wide will the output vector be
    window = int(len(input_v) / expected_width)

    output_v = []
    offset = 0
    for i in range(expected_width):
        output_v.append(np.mean(input_v[ offset+i*window : offset+(i+1)*window]))
    return output_v
