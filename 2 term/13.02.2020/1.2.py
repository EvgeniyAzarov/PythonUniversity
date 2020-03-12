import math
class VectorNd:
    def __init__(self, coords):
        if isinstance(coords, VectorNd):
            self._coords = coords._coords
        else:
            self._coords = coords
    
    def len(self):
        return len(self._coords)

    def mean(self):
        m = 0.0
        for i in self._coords:
            m += i
        m /= self.len()
        return m

    def min(self):
        m = math.inf
        for i in self._coords:
            if i < m:
                m = i
        return m

    def max(self):
        m = -math.inf
        for i in self._coords:
            if i > m:
                m = i
        return m

    def print(self):
        for i in self._coords:
            print(i, end=' ')
        print()



coords = tuple(map(float, input().split()))

vec1 = VectorNd(coords)
vec = VectorNd(vec1)

vec.print()
print(vec.len())
print(vec.max())
print(vec.min())
print(vec.mean())

