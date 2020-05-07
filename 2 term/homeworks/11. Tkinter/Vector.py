class Vector:
    def __init__(self, n):
        self.n = n
        self.vec = [None for i in range(n)]

    def set(self, vec):
        assert len(vec) == self.n
        self.vec = vec

    def len(self):
        return self.n
