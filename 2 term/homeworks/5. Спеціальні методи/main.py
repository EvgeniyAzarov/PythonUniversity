from complex import Complex

a, b, c, d, e, f = map(float, input().split())

A = Complex(a, b)
B = Complex(c, d)
C = Complex(e, f)

print("x1 = ", (((B**2 - A*C*4)**0.5) - B)/(A*2))
print("x2 = ", (Complex(0, 0) - ((B**2 - A*C*4)**0.5) - B)/(A*2))
