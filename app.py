from linearity import *
from evenOdd import *
from evenOddDecompose import *

# testing

f = lambda x: 2 * x
x1 = lambda x: x
x2 = lambda x: 2 * x
linear(f, x1, x2, 0, 4)

g = lambda x:  sin( 2*3.14/10 * x )
even_odd(f, -5, 5)

h = lambda x: 2**x
even_odd_decompose(h, -5, 5)