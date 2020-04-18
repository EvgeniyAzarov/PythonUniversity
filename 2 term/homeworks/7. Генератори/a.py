def SequenceGenerator(x, n):
    yield -x
    xk = -x
    for i in range(1, n):
        xk *= -x * i / (i + 1)
        yield xk


x = float(input("x = "))
k = int(input("k = "))

for a in SequenceGenerator(x, k):
    print(a)
