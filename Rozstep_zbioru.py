"""
Rozstęp zbioru liczb
"""

def range(numbers):
    highest = max(numbers)
    lowest = min(numbers)
    r = highest -lowest

    print(f"Wartość max: {highest}" )
    print(f"wartośc min: {lowest}")
    print(f"Rozstęp: {r}")

li = [1, 2, 3, 5, 6, 7, 7, 10]
f = range(li)
print(f)