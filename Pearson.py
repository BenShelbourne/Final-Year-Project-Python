import codecs
import csv
import math

RAW_DATA = ['Boeing 1998-2005.csv','Lockheed Martin 1998-2005.csv']
data = []
results = []

def setup():
    for raw_csv in RAW_DATA:
        data.append(read_file(raw_csv))

def matrix():
    x = 0
    y = len(data) - 1
    while x < len(data):
        results.append([])
        while y > 0:
            if x == y:
                y -= 1
                continue
            results[x].append(pearson_def(data[x], data[y]))
            y -= 1
        x += 1

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
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
    content = []
    with codecs.open(file, encoding="utf-8-sig") as f:
        for x in f:
            content.append(float(x.strip()))
    return content

if __name__ == "__main__":
    setup()
    matrix()
    print(results)