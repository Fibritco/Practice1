"""
średnia z pliku
"""

def read_data(file):
    num = []
    with open(file) as f:
        for line in f:
            num.append(float(line))
    return num

def mean(num):
    s = sum(num)
    N = len(num)
    return s/N