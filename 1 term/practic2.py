n = int(input())

print(n % 2 == 0)
print(n % 10 == 0)
print(n % 10 + (n // 10) % 10 > 9)

x = float(input())
y = float(input())

print(2 >= (x * x + y * y) ** 0.5 >= 1)

m = int(input())

print(m % 10 == 2 or (m // 10) % 10 == 2 or (m // 100) % 10 == 2)
print((m % 10) % 2 == 0 and ((m // 10) % 10) % 2 == 0 and ((m // 100) % 10) % 2 == 0)
print((m % 10) + ((m // 10) % 10) + ((m // 100) % 10) == 18)

x = float(input())

print(0 if x <= 0 else (x * x if 0 < x <= 1 else x ** 4))

# ------------------------------------------------------------------------------

a = float(input())

if a == 0:
    print("Немає розв'язків.")
else:
    print("x in ({}, {}), y = 1".format(-2/a, 2/a))

