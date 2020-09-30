import numpy as np
import matplotlib.pyplot as plt

def plot_seq(x, y, b=None, eps=0.01, localPlot=False):
    if (b is None):
        plt.plot(x, y, ".b")
        
        y_min = np.amin(np.array(y[begin:]))
        y_max = np.amax(np.array(y[begin:]))
        plt.axis([x[begin], x[-1], y_min, y_max])

        return y[-1]
    else:
        k = -1
        prev = False
        for i in range(y.size):
            if abs(y[i]-b) < eps:
                if not prev:
                    k = i
                    prev = True
            else:
                prev = False

        if not prev:
            return

        begin = 0 if not localPlot else k

        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")

        plt.xlabel("n")
        plt.ylabel("a(n)")

        plt.axis([x[begin], x[-1], b-2*eps, b+2*eps])

        return x[k]


def vec_y(x):
    return ((x-1)**4-(x+2)**4)/((2*x+1)**3+(x-1)**3)

    
if __name__ == "__main__":
    x = np.arange(1, 10000, 100)
    y = vec_y(x)

    #print(plot_seq(x, y))
    print(plot_seq(x, y, -4/3, 0.001, False))
    plt.show()
