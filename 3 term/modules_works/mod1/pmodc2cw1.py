import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def construct_f1(a, b):
    def _f1(x):
        return a*x+b
    return _f1


def f2(x):
    return (x-1)**2


POINTS_NUM = 5000
def mc_square(f1, f2, xmin, xmax, ymin, ymax):
    box_square = (xmax-xmin)*(ymax-ymin)
    count = int(box_square) * POINTS_NUM
    x = np.random.uniform(xmin, xmax, count)
    y = np.random.uniform(ymin, ymax, count)
    y1 = f1(x)
    y2 = f2(x)
    count_in = len(y[np.logical_and(y2 <= y, y <= y1)])

    return box_square * count_in / count


def plotf1f2(u, v, n, f1, f2):
    x = np.linspace(u, v, n)
    y1 = f1(x)
    y2 = f2(x)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.fill_between(x, y1, y2, where=(y1-y2)>=0, facecolor="green")

    a0, b0, c0, d0 = plt.axis()
    square = mc_square(f1, f2, a0, b0, c0, d0)
    print("Area of green figure: ", square)

    plt.show()


if __name__ == "__main__":
    a = float(input("a = "))
    b = float(input("b = "))

    D = (a+2)**2-4*(1-b)
    if D < 0:
        print("Фігури немає")
        exit()

    u = (a+2-sqrt(D))/2 
    v = (a+2+sqrt(D))/2

    print(u, v)
    plotf1f2(u-1, v+1, 100, construct_f1(a, b), f2)

    
