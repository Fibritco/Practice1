"""
Większa ilość dominant, wtedy kod poniżej:
"""

from collections import Counter

def cal_mode_milti(numbers):
    c = Counter(numbers)
    num_freq = c.most_common()
    max_count = num_freq[0][1]

    dominanty = []
    for i in num_freq:
        if i[1] == max_count:
            dominanty.append(i[0])
    return dominanty


li = [6, 6, 6, 4, 4, 4, 9, 2, 3]
modes = cal_mode_milti(li)
print(f'Dominanty:')
for i in modes:
    print(i)