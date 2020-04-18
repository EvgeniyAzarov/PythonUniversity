import math


def cosh(x, e):
    u = 1
    v = x ** 2 / 2
    s = u + v
    k = 3
    while u - v > e:
        u = v
        v *= x ** 2 / (k * (k + 1))
        k += 2
        s += v
    return s


x = float(input("x = "))
e = float(input("e = "))

print(math.cosh(x))
print(math.cosh(x) - cosh(x, e))
