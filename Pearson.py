import math
import pandas as pd
import csv
import codecs

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    print(x)
    avg_x = average(x)
    avg_y = average(y)
    diff_prod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diff_prod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diff_prod / math.sqrt(xdiff2 * ydiff2)

def read_file(file):
    with codecs.open(file, encoding="utf-8-sig") as f:
        w, h = [float(x) for x in next(f).split()]
        array = [[float(x) for x in line.split()] for line in f]
        array = array.shift()


    
    return array

Boeing = read_file('Boeing 1998-2005.csv')
Lockheed = read_file('Lockheed Martin 1998-2005.csv')


print (pearson_def (Boeing, Lockheed))

