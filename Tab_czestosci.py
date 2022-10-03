"""
Tabela częstości 
"""


from collections import Counter

def freq_tab(numbers):
    tab = Counter(numbers)
    print('Numbers\tOccurrence')
    for i in tab.most_common():
        print(f'{i[0]}\t{i[1]}')


li = [1, 2, 2, 2, 2, 4, 4, 4, 5, 8, 12, 15, 12, 1, 2]
freq_tab(li)