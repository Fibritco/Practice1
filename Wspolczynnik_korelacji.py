"""
Współczynnik korelacji = [ n * suma(xy) - suma(x)*suma(y) ] / [(n * suma(x**2) - suma(x)**2)  *  (n * suma(y**2) - suma(y)**2)]**0.5
"""

def find_corr_x_y(x, y):
    n = len(x)

    # Suma iloczynów
    prod = []
    for u1, u2 in zip(x,y):
        prod.append(u1 * u2)
    sum_prod_x_y = sum(prod)

    sum_x = sum(x)
    sum_y = sum(y)
    sq_sum_x = sum_x ** 2
    sq_sum_y = sum_y ** 2

    # Suma
    x_sq = []
    for i in x:
        x_sq.append(i ** 2)
    x_sq_sum = sum(x_sq)
    
    # Suma
    y_sq = []
    for i in x:
        y_sq.append(i ** 2)
    y_sq_sum = sum(y_sq)

    # współczynnik korelacji obliczenia
    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator_1 = n * x_sq_sum - sq_sum_x
    denominator_2 = n * y_sq_sum - sq_sum_y
    demininator = (denominator_1 * denominator_2) ** 0.5

    correlation = numerator / demininator
    return correlation


l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5, 6]

a = find_corr_x_y(l1, l2)
print()
print(a)
print()