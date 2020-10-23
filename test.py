import random
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

fig = Figure()
axis = fig.add_subplot(1, 1, 1)
xs = range(100)
ys = [random.randint(1, 50) for x in xs]
axis.plot(xs, ys)
plt.show()

# testing

f = lambda x: 2 * x
x1 = lambda x: x
x2 = lambda x: 2 * x
linear(f, x1, x2, 0, 4)

g = lambda x:  sin( 2*3.14/10 * x )
even_odd(f, -5, 5)

h = lambda x: 2**x
even_odd_decompose(h, -5, 5)