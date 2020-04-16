R = "R"


class Eq:
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def solve(self):
        if self.b == 0:
            if self.c != 0:
                return tuple()
            else:
                return R
        else:
            return -self.c / self.b,

    def show(self):
        return "{}*x + {} = 0".format(self.b, self.c)


class QuEq(Eq):
    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def solve(self):
        if self.a == 0:
            return super().solve()
        else:
            d = self.b * self.b - 4 * self.a * self.c
            if d > 0:
                return (-self.b - d ** 0.5) / (2 * self.a), (-self.b + d ** 0.5) / (2 * self.a)
            elif d == 0:
                return (-self.b - d ** 0.5) / 2
            else:
                return tuple()

    def show(self):
        return "{}*x^2 + {}*x+{} = 0".format(self.a, self.b, self.c)


class BiQuEq(QuEq):
    def __init__(self, a, m, b, n, c):
        super().__init__(a, b, c)

    def solve(self):
        res = super().solve()
        if isinstance(res, tuple):
            r = []
            for a in res:
                if a >= 0:
                    r.append(a ** 0.5)
                    r.append(-a ** 0.5)
            return tuple() if r == [] else r

        else:
            return res


eqs = []

with open('classworks/27.02.2020/eqs.txt') as file:
    for line in file:
        coef = tuple(map(float, line.split()))
        if len(coef) == 2:
            eq = Eq(*coef)
            eqs.append(eq)
        elif len(coef) == 3:
            eq = QuEq(*coef)
            eqs.append(eq)
        elif len(coef) == 5:
            eq = BiQuEq(*coef)
            eqs.append(eq)

types = {"inf": [], 0: [], 1: [], 2: [], 3: [], 4: []}

for e in eqs:
    s = e.solve()
    if s == R:
        types["inf"].append(e.show())
    else:
        types[len(s)].append(e.show())

print(types)
