def product_generator(n):
    yield 2/3
    cur = 2/3
    for i in range(2, n+1):
        cur *= (i + 1) / (i + 2)
        yield cur


n = int(input("n = "))

for t in product_generator(n):
    print(t)
