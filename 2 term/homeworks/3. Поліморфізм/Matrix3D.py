from Matrix import Matrix
from Matrix2D import Matrix2D


class Matrix3D(Matrix):
    def __init__(self, m=3):
        super().__init__(m)

    def det(self):
        m = [Matrix2D() for i in range(3)]
        m[0].set([[self.matrix[1][1], self.matrix[1][2]],
                  [self.matrix[2][1], self.matrix[2][2]]])
        m[1].set([[self.matrix[1][0], self.matrix[1][2]],
                  [self.matrix[2][0], self.matrix[2][2]]])
        m[2].set([[self.matrix[1][0], self.matrix[1][1]],
                  [self.matrix[2][0], self.matrix[2][1]]])

        res = 0
        for i in range(3):
            res += (-1) ** i * self.matrix[0][i] * m[i].det()

        return res
