import marimo

__generated_with = "0.2.5"
app = marimo.App()


@app.cell
def __():
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    import glob
    import os

    l0 = glob.glob('./im/2001/*.png')
    l1 = glob.glob('./im/2022/*.png')

    for i in range(0, len(l0)):
        ma = np.array(Image.open(l0[i]))
        mb = np.array(Image.open(l1[i]))
        md = np.concatenate((ma, mb), axis=0)
        Image.fromarray(md).save('./im/cmb/comb' + os.path.split(l0[i])[1])
    return Image, glob, i, l0, l1, ma, mb, md, np, os, plt


@app.cell
def __(Image, glob):
    files = sorted(glob.glob('./im/cmb/comb*.png'))  
    images = list(map(lambda file : Image.open(file), files))
    images[0].save('./im/cmb/comb0122.gif', save_all = True, 
            append_images = images[1:], duration = 1200, loop = 0)
    return files, images


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
