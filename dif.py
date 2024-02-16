import marimo

__generated_with = "0.2.5"
app = marimo.App()


@app.cell
def __():
    import glob
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    import os

    l = glob.glob('./im/2001/*.png')
    m = []
    for i in l:
        m.append(np.array(Image.open(i), dtype='u1'))

    np.save('./im/cmb/2001all', m)
    return Image, glob, i, l, m, np, os, plt


@app.cell
def __(np):
    mx = np.load('./im/cmb/2001all.npy')
    print(mx.shape)
    print(mx.dtype)
    return mx,


@app.cell
def __(np, plt):
    im = np.load('./im/cmb/2001all.npy')
    s = im[0, :, :].astype(np.float64)
    for j in range(1, len(im)):
        s += im[j, :, :]
    s = s / 12
    plt.imshow(s, cmap="gray")
    return im, j, s


@app.cell
def __(Image, glob, i, np):
    l2 = glob.glob('./im/2022/*.png')
    m2 = []
    for k in l2:
        m2.append(np.array(Image.open(i), dtype='u1'))

    np.save('./im/cmb/2022all', m2)
    return k, l2, m2


@app.cell
def __(im, np, plt, s):
    im2 = np.load('./im/cmb/2022all.npy')
    s2 = im2[0, :, :].astype(np.float64)
    for a in range(1, len(im)):
        s2 += im[a, :, :]
    s2 = s2 / 12
    plt.imshow(s, cmap="gray")
    return a, im2, s2


@app.cell
def __(np, plt, s, s2):
    sc = np.concatenate((s, s2), axis=0)

    plt.imshow(sc, cmap="gray")
    return sc,


@app.cell
def __(plt, s, s2):
    thresh = 0
    sb = s2 - s
    sb = sb >= thresh

    plt.imshow(sb, cmap="gray")
    return sb, thresh


@app.cell
def __(np, plt, sb, sc):
    sd = np.concatenate((sc, sb *255), axis=0)

    plt.imshow(sd, cmap="gray")
    plt.imsave('./im/cmb/average0122.png', sd, cmap="gray")
    return sd,


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
