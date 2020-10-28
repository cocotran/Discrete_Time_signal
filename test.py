import random
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import re

from signals.evenOdd import *
from signals.evenOddDecompose import *
from systems.linearity import *
from systems.timeVariant import *

# fig = Figure()
# axis = fig.add_subplot(1, 1, 1)
# xs = range(100)
# ys = [random.randint(1, 50) for x in xs]
# axis.plot(xs, ys)
# plt.show()

# testing
funcF = 'x(t)**2'
funcG = funcF.replace('(t)', '(t-k)')
k = random.randint(-10, 10)
x = lambda t: t
f = lambda t: eval(funcF)
g = lambda t: eval(funcG)
time_invariant(f, g, x, k, -2, 4)

# f = lambda x: x**2
# x1 = lambda x: x
# x2 = lambda x: 2 * x
# linear(f, x1, x2, 0, 4)

# g = lambda x: sin(2 * 3.14 / 10 * x)
# even_odd(f, -5, 5)

# h = lambda x: 2**x
# even_odd_decompose(h, -5, 5)