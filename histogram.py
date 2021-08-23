from PIL import Image
import numpy as np


def histogram(image):
    h = [0] * 256

    for i in image:
        for j in i:
            h[j] = h[j] + 1

    return h

def normalized_historgram(hist, width, height):
    nhist = []
    x = width * height

    for i in range(255):
        nhist.append(hist[i] / x)

    return nhist
