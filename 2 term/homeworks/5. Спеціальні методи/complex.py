import math

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        return "{} + {}i".format(self.re, self.im)

    def __add__(self, other):
        if isinstance(other, Complex):
            re = self.re + other.re
            im = self.im + other.im
        else:
            re = self.re + other
            im = self.im

        return Complex(re, im)

    def __sub__(self, other):
        if isinstance(other, Complex):
            re = self.re - other.re
            im = self.im - other.im
        else:
            re = self.re - other
            im = self.im

        return Complex(re, im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + self.im * other.re
        else:
            re = self.re * other
            im = self.im * other

        return Complex(re, im)

    def __truediv__(self, other):
        assert other.re != 0 or other.im != 0

        if isinstance(other, Complex):
            re = (self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im ** 2)
            im = (-self.re * other.im + self.im * other.re) / (other.re ** 2 + other.im ** 2)
        else:
            re = self.re / other
            im = self.im / other

        return Complex(re, im)

    def __pow__(self, other):
        if self.re == self.im and self.im == 0:
            return Complex(0, 0)
        m = math.sqrt(self.re ** 2 + self.im ** 2)
        x = math.acos(self.re / m)
        y = math.asin(self.im / m)

        return Complex(m ** other * math.cos(x * other), m ** other * math.sin(y * other))

