class Matrix:
    def __init__(self, n):
        if isinstance(n, Matrix):
            self.n = n.n
            self.matrix = [[None for i in range(self.n)] for j in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    self.matrix[i][j] = n.matrix[i][j]
        else:
            self.n = n
            self.matrix = [[None for i in range(self.n)] for j in range(self.n)]

    def read(self):
        for i in range(self.n):
            row = list(map(float, input().split()))
            assert len(row) == self.n
            self.matrix[i] = row

    def read_from_file(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            assert len(lines) >= self.n
            for i in range(self.n):
                self.matrix[i] = list(map(float, lines[i].split()))

    def print(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.matrix[i][j], end=' ')
            print()
        print()

    def print_to_file(self, filename):
        with open(filename, 'x') as file:
            for i in range(self.n):
                for j in range(self.n):
                    print(self.matrix[i][j], end=' ', file=file)
                print(file=file)
            print(file=file)

    def set(self, a):
        assert len(a) == self.n
        assert len(a[0]) == self.n

        self.matrix = a

    def set_row(self, r, pos):
        assert len(r) == self.n
        for i in range(self.n):
            self.matrix[i][pos] = r[i]

    def det(self):
        pass

    def is_singular(self):
        return self.det() == 0

    def get_matrix(self):
        return self.matrix
