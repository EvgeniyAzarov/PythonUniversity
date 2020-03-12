class Vector:
    def __init__(self, n):
        self.n = n
        self.vec = [None for i in range(n)]

    def read_from_file(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            assert len(lines[-1].split()) == self.n
            self.vec = list(map(float, lines[-1].split()))

    def set(self, vec):
        assert len(vec) == self.n
        self.vec = vec

    def print(self):
        for i in range(self.n):
            print(self.vec[i], end=' ')
        print()

    def len(self):
        return self.n

    def get_list(self):
        return self.vec


class Vector2D(Vector):
    def __init__(self):
        super().__init__(2)


class Vector3D(Vector):
    def __init__(self):
        super().__init__(3)
