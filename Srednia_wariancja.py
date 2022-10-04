"""
Średnia + Wariancja
"""


def mean_(numbers):
    N = len(numbers)
    s = sum(numbers)
    mean = s/N

    return mean

def difference_(numbers):
    mean = mean_(numbers)

    li = []
    # odchył od średniej
    for i in numbers:
        li.append(i - mean)

    return li

def variance_(numbers):
    # lista rożnic
    li = difference_(numbers)
    # kwadrat różnic
    sq_li = []
    for i in li:
        sq_li.append(i ** 2)

    # Wariancja
    sum_sq_li = sum(sq_li)
    varian = sum_sq_li/len(numbers)
    return varian

lii = [1, 2, 3, 5, 7, 3, 5, 6, 8, 9, 1, 1, 10]

# odchylenie standardowe 
varian = variance_(lii)
std =  round(varian ** 0.5, 2)



m = round(mean_(lii), 2)
d = [round(i, 2) for i in difference_(lii)]
v = round(variance_(lii), 2)

print(f'Średnia: {m}\n\nRóżnica od średniej: {d}\n\nWariancja: {v}\n\nOdchylenie standardowe: {std}')
