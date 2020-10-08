import numpy as np
import matplotlib.pyplot as plt


NUM = 5000

def fun_cos(n):
    def _func(x):
        p = np.ones_like(x)
        s = np.ones_like(x)
        for k in range(2, n + 1):
            p *= -x**2 / ((2*k-3)*(2*k-2))
            s += p
        return s
    return _func
   

def mc_square(f1, f2, xmin, xmax, ymin, ymax):
    box_square = (xmax - xmin) * (ymax - ymin)
    count = int(box_square) * NUM
    x = np.random.uniform(xmin, xmax, count)
    y = np.random.uniform(ymin, ymax, count)
    y1 = f1(x)
    y2 = f2(x)
    count_in = len(y[np.logical_or(
        np.logical_and(y1 <= y, y <= y2),
        np.logical_and(y2 <= y, y <= y1))])

    return box_square * count_in / count, box_square


def movespinesticks():
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["left"].set_position(("data", 0))


def plotf1f2(a, b, n, f1, f2):
    x = np.linspace(a, b, n)
    y1 = f1(x)
    y2 = f2(x)

    plt.subplot(2, 1, 1)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.fill_between(x, y1, y2, where=np.abs(y2 - y1) >= 0, facecolor="green")

    a0, b0, c0, d0 = plt.axis()
    square, box_square = mc_square(f1, f2, a0, b0, c0, d0)
    print("Deviation: ", np.sqrt(square / box_square))

    movespinesticks()
    #plt.xlabel("x")
    #plt.ylabel("y")

    ydif = np.abs(y2 - y1)

    plt.subplot(2, 1, 2)
    plt.plot(x, ydif, label="diff")

    movespinesticks()
    #plt.xlabel("x")
    #plt.ylabel("y")
    plt.legend(loc="best")

    plt.show()

#
#if __name__ == '__main__':
#    a = -2*np.pi
#    b = 2*np.pi;
#    m = 5
#    plotf1f2(a, b, 1000, np.sin, func_cos(m))
#
if __name__ == "__main__":
    a = -2*np.pi
    b = 2*np.pi
    m = 5
    plotf1f2(a, b, 1000, np.cos, fun_cos(m))
    #plotf1f2(a, b, 1000, np.cos, np.cos)
    
 
