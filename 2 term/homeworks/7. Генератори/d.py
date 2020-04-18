def sum_generator(m):
    a1 = 1
    a2 = 1
    b = 3
    s = b
    yield s
    b = 9
    s += b
    yield s
    for i in range(3, m + 1):
        a1, a2 = a2, a2 / i + a1
        b *= 3 / a2
        s += b
        yield s


n = int(input("n = "))

for t in sum_generator(n):
    print(t)
