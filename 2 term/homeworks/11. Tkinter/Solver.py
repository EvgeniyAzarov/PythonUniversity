from Matrix import Matrix
import copy

class Solver:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = b.len()

    def solve(self):
        if self.a.is_singular():
            raise ValueError('There is no unique solution')
        sol = []
        det = self.a.det()
        t = Matrix(self.n)
        for i in range(self.n):
            t.set(copy.deepcopy(self.a.matrix))
            t.set_column(self.b.vec, i)
            sol.append(t.det() / det)

        for i in range(self.n):
            sol[i] = f"x{i+1} = " + str(sol[i])
        return sol
