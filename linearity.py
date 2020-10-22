# checks to see if a given system is satisfies the additive property of linear systems

# Algorithm
# given an input signal x1[n], the output response produced is y1[n] and
# given an input signal x2[n], the output response produced is y2[n],
# then for an input signal x3[n] = x1[n] + x2[n], the output response y3[n] = y1[n] + y2[n]

from math import *
import matplotlib.pyplot as plt

# parameter: system function, input x1, input x2, interval from, interval to
def linear(f, x1, x2, n_from: int, n_to: int):
	# define n
    n = [i for i in range(n_from, n_to + 1)]

    # define x1[n]
    x_1 = [x1(i) for i in n]
    # define x2[n]
    x_2 = [x2(i) for i in n]

    # output response produced by input x1
    y_1 = [f(i) for i in x_1]
    # output response produced by input x2
    y_2 = [f(i) for i in x_2]

    # sum of two output y1 and y2
    y_1_2 = [y_1[i] + y_2[i] for i in range(len(y_1))]

    # define x3[n] = A*x1[n] + B*x2[n]
    # for simplicity make A = B = 1
    x_3 = [(x_1[i] + x_2[i]) for i in range(len(x_1))]

    # define output response y_3
    y_3 = [f(i) for i in x_3]

    isEqual = False
    for i in range(len(y_3)):
        if (y_3[i] == y_1_2[i]):
            isEqual = True
        else:
            isEqual = False

    if isEqual:
        print('Outputs are consistent with a linear system')
    else:
        print('System is not linear')

    # ploting stuffs
    fig, axs = plt.subplots(ncols=2,
                            nrows=1,
                            constrained_layout=True,
                            sharey=True)
    axs[0].stem(n, y_1_2)
    axs[0].set(xlabel='n', ylabel='Output responses', title='y1[n] + y2[n]')
    axs[1].stem(n, y_3)
    axs[1].set(xlabel='n', title='y3[n]')
    fig.suptitle('Stem plots of the responses')
    plt.show()
