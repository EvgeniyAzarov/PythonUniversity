from Matrix import Matrix


class Matrix2D(Matrix):
    def __init__(self):
        super().__init__(2)

    def det(self):
        return self.matrix[0][0] * self.matrix[1][1] - \
            self.matrix[1][0] * self.matrix[0][1]