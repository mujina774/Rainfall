import glob
import os
import sys
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def listing(path):
    if not os.path.isfile(path + 'RenderData (0).png'):
        if os.path.isfile(path + 'RenderData.png'):
            os.rename(path + 'RenderData.png', path + 'RenderData (0).png')
        else:
            print('no RenderData (0).png in %s' % path )
            return

def rename(p, ii, px, e):
    f = sorted(glob.glob(path + '*' + e), key = natural_keys)
    i = 1
    for fn in f:
        st = str(i).zfill(2)
        os.rename(fn, p + px + ii + st + e)
        i += 1

prefix = 'rf'
ext = '.png'
y = range(2001, 2002)
for i in y:
    path = './im/' + str(i) + '/'
#    listing(path)
    rename(path, str(i), prefix, ext)

    f = glob.glob(path + '*' + ext)
    for j in f:
        print(j)