import numpy as np
import histogram as h

def binarize(image, seuil=127, foreground=255):
    binarised_img = np.zeros([len(image), len(image[0])], dtype=np.int)

    for i in range(len(image)):
        for j in range(len(image[0])):
            binarised_img[i, j] = foreground if image[i, j] > seuil else 0

    return binarised_img


def otsu(image):
    nhist = h.normalized_historgram(
        h.histogram(image), len(image), len(image[0])
    )
    vmax = 0
    tmax = 1

    for t in range(1, len(nhist)):
        q1 = np.sum(nhist[0: t])
        q2 = 1 - q1

        # u1 = sum i*P(i) / q1
        j = 0
        u1 = 0
        for j in range(t - 1):
            u1 = u1 + j * nhist[j]
        if u1 > 0:
            u1 = u1 / q1

        j = t + 1
        u2 = 0
        for j in range(t, 255):
            u2 = u2 + j * nhist[j]
        if u2 > 0:
            u2 = u2 / q2
        vb = q1 * q2 * (u1 - u2) * (u1 - u2)

        if vb > vmax:
            vmax = vb
            tmax = t

    return tmax
