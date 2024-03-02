import marimo

__generated_with = "0.2.5"
app = marimo.App()


@app.cell
def __():
    import glob
    import os
    import re

    path = './im/2022/'
    pf = 'rf'

    def atoi(text):
        return int(text) if text.isdigit() else text

    def natural_keys(text):
        return [ atoi(c) for c in re.split(r'(\d+)', text) ]

    flist = glob.glob(path + '*.png')
    sf = sorted(flist, key = natural_keys)
    sf
    return atoi, flist, glob, natural_keys, os, path, pf, re, sf


@app.cell
def __(os, path, pf, sf):
    j = 1

    for file in sf:
        st = str(j).zfill(2)
        os.rename(file, path + pf + st + '.png')
        j+=1
    return file, j, st


@app.cell
def __(glob, path):
    fo = glob.glob(path + '*.png')
    for k in fo:
        print(k)
    return fo, k


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
