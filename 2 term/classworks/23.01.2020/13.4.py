def read_matrix(file):
    with open(file) as f:
        m = []
        for line in f:
            m.append(list(map(float, line.split())))

        return m

def write_matrix(file, m):
    f = open(file, 'w')
    for line in m:
        f.write(" ".join(map(str,line)))
        f.write("\n")
    f.close()

a = read_matrix('classworks/23.01.2020/a.txt')
b = read_matrix('classworks/23.01.2020/b.txt')

if len(a[0]) != len(b) or len(a) != len(b) or len(a[0]) != len(b[0]):
    print("Incorrect input data")

m = len(a)
n = len(b[0])

ab = [[None for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        ab[i][j] = 0
        for k in range(len(a[0])):
            ab[i][j] += a[i][k] * b[k][j]

write_matrix("classworks/23.01.2020/ab.txt", ab)

