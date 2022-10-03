"""
Tabela częstości + sortowanie
"""


from collections import Counter

def freq_tab(numbers):
    tab = Counter(numbers)
    num_so = tab.most_common()
    num_so.sort()

    print('Numbers\tOccurrence')
    for i in num_so:
        print(f'{i[0]}\t{i[1]}')


li = [1, 2, 2, 2, 2, 4, 4, 4, 5, 8, 12, 15, 12, 1, 2]
freq_tab(li)