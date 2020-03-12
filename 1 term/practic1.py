print("  *  \n *** \n*****\n *** \n  *  ")

m1 = float(input())
m2 = float(input())
r = float(input())

print(6.67 * 10 ** (-12) * m1 * m2 / (r * r))

m1 = m1 + m2
m2 = m1 - m2
m1 = m1 - m2

print(m1, m2)

n = int(input())
s = 0
m = 0

while n > 0:
    s += (n % 10)
    m *= 10
    m += (n % 10)
    n //= 10

print(s)
print(m)

z = complex(1, 5)
u = z.conjugate()

print(u)

# ДЗ: (Если несколько пунктов, то тот, что по модулю с номером в группе)
