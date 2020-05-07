import copy

class Matrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[None for i in range(self.n)] for j in range(self.n)]

    def __str__(self):
        res = ''
        
        for i in range(self.n):
            for j in range(self.n):
                res += str(self.matrix[i][j]) + ' '
            res += '\n'
        res += '\n'

        return res

    def set(self, a):
        assert len(a) == self.n
        assert len(a[0]) == self.n

        self.matrix = a

    def set_column(self, r, pos):
        assert len(r) == self.n
        for i in range(self.n):
            self.matrix[i][pos] = r[i]

    @staticmethod
    def _minor(M, i, j):
        A = copy.deepcopy(M)
        del A[i]
        for i in range(len(M) - 1):
            del A[i][j]

        return A

    @staticmethod   
    def _det(M):

        if len(M) == 1:
            return M[0][0]

        res = 0

        sign = 1
        for i in range(len(M)):
            res += sign * M[0][i] * Matrix._det(Matrix._minor(M, 0, i))
            sign *= -1
        
        return res

    def det(self):
        res = 0
        
        return self._det(self.matrix)

    def is_singular(self):
        return self.det() == 0

