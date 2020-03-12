a,b,c = map(float, input().split())
d = b**2 - 4*a*c
assert a != 0 and d >= 0

if d == 0:
    print(-b/(2*a))
else:
    print((-b-d**0.5)/(2*a), (-b+d**0.5)/(2*a))
