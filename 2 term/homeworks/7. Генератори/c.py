def det(x, N):
    d2 = x ** 2 + 1
    d1 = x ** 4 + x ** 2 + 1

    for i in range(3, N + 1):
        d2, d1 = d1, (1 + x ** 2) * d1 - x ** 2 * d2

    return d1


x = float(input("x = "))
n = int(input("n = "))

print(det(x, n))
