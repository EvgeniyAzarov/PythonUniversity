import numpy as np

n = int(input("n = "))
a = [list(map(float, input().split(" "))) for i in range(n)]

#a = np.arange(1, 10).reshape(3, 3)

a = np.array(a)

x = np.sum(a, 1)
y = np.sum(a, 0)
u = np.hstack((x, y))

s = u[0]

print(np.size(u[u==s]) == 2*n)
