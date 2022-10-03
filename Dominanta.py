"""
Wyznaczanie dominanty
"""

from collections import Counter


def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
mode = calculate_mode(scores)
print(f"Dominanta: {mode}")

'''

if __name__ == "__name__":
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    mode = calculate_mode(scores)
    print(f"Dominanta: {mode}")

'''
