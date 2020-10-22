# determines if a signal x[n] = function(n)
# is even or odd
# also decomposes the original signal into its even and odd components

# x[n] is EVEN is x[n] = x[-n]
# x[n] is ODD if x[n] = -x[-n]

from math import *
import matplotlib.pyplot as plt

# parameter: signal function, interval from, interval to
def even_odd(f, n_from: int, n_to: int):
	# define n
	n = [i for i in range(n_from, n_to + 1)]
	# define -n
	n_inverse = [(i*-1) for i in n]

	# define x1[n]
	x_1 = [f(i) for i in n]
	# define x2 = x1[-n]
	x_2 = [f(i) for i in n_inverse]

	isType = 'Even'
	for i in range(len(n)):
		if (x_1[i] == x_2[i]):
			isType = "Even"
		if (x_1[i] == (x_2[i]*-1)):
			isType = "Odd"
		else:
			isType = "Neither"

	print(isType)
	fig, axs = plt.subplots(ncols=2,nrows=1, constrained_layout=True, sharey=True)
	axs[0].stem(n, x_1)
	axs[0].set(xlabel='n', ylabel='x[n]')
	axs[1].stem(n, x_2)
	axs[1].set(xlabel='n', ylabel='x[-n]')
	plt.show()
