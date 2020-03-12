from Matrix3D import Matrix3D


class Solver:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = b.len()

    def solve(self):
        if self.a.is_singular():
            return "infinity"
        sol = []
        for i in range(self.n):
            t = Matrix3D(self.a)
            t.set_row(self.b.get_list(), i)
            sol.append(t.det() / self.a.det())
        return sol
