# decompose the signal into its
# even and odd components
# using the definitions
# even component = (1/2) * ( x[n] + x[-n])
# odd component = (1/2) * ( x[n] - x[-n])

from math import *
import matplotlib.pyplot as plt

# parameter: signal function, interval from, interval to
def even_odd_decompose(f, n_from: int, n_to: int):
	# define n
	n = [i for i in range(n_from, n_to + 1)]
	# define -n
	n_inverse = [(i*-1) for i in n]

	# define x1[n]
	x_1 = [f(i) for i in n]
	# define x2 = x1[-n]
	x_2 = [f(i) for i in n_inverse]

	even_comp = [0.5*(x_1[i] + x_2[i])  for i in range(len(n))]
	odd_comp = [0.5*(x_1[i] - x_2[i])  for i in range(len(n))]
	fig, axs = plt.subplots(ncols=2,nrows=1, constrained_layout=True, sharey=True)
	axs[0].stem(n, even_comp)
	axs[0].set(xlabel='n', ylabel='Even component of x[n]')
	axs[1].stem(n, odd_comp)
	axs[1].set(xlabel='n', ylabel='Odd component of x[n]')
	plt.show()
