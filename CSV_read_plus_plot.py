"""
CSV read and plot
"""

import csv
import matplotlib.pyplot as plt

def plot_scatter(x, y):
    plt.scatter(x, y)
    plt.xlabel("x_label")
    plt.ylabel("Y_label")
    plt.title("Title")
    plt.show()

def read_csv(file):
    num = []
    squ = []
    with open(file) as f:
        reader = csv.reader(f)
        next(reader) # table title etc.
        for i in reader:
            num.append(int(i[0]))   # first linr
            squ.append(int(i[1]))   # second line

    num, squ = read_csv('Some file.csv') # add file name and path