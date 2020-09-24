from benchmark import benchmark_class
import numpy as np


@benchmark_class
class FibRealisations:
    def __init__(self, n):
        self.n = n

    def fib_v1(self):
        a = 1
        b = 1
        for i in range(self.n - 2):
            a = a + b
            a, b = b, a

        return b

    def fib_v2(self):
        m = np.array([0,1,1,1]).reshape(2,2)
        res = np.linalg.matrix_power(m, self.n-1)[1, 1]
        return res
