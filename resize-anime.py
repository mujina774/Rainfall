import marimo

__generated_with = "0.2.5"
app = marimo.App()


@app.cell
def __():
    import numpy as np
    import glob
    import os
    from PIL import Image

    files = sorted(glob.glob('./im/2002/*.png'))  
    images = list(map(lambda file : Image.open(file), files))
    images[0].save('./im/2002/image.gif', save_all = True, append_images = images[1:], duration = 1200, loop = 0)


    return Image, files, glob, images, np, os


@app.cell
def __(Image, glob, np, os):
    l = glob.glob('./im/2023/*.png')
    for i in l:
        d = './im/2023/sm/'+ os.path.split(i)[1]
        im = Image.open(i)  
        r = im.resize((np.array(im.size)/2).astype(int)) 
        s = np.array(r)
        Image.fromarray(s).save(d)
    return d, i, im, l, r, s


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
