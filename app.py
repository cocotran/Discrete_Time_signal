from systems.linearity import *
from signals.evenOdd import *
from signals.evenOddDecompose import *
from systems.timeVariant import *

import random
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/even_odd_decomposition.png')
def evenOddDecompose():
    fig = evenOddDecompose_plot()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def evenOddDecompose_plot():
    f = lambda x: 2**x
    data = even_odd_decompose(f, -5, 5)
    fig = Figure()
    axis = fig.add_subplot(1, 2, 1)
    axis.stem(data[0], data[1])
    axis.set(xlabel='n', title='Even component of x[n]')
    axis = fig.add_subplot(1, 2, 2)
    axis.stem(data[0], data[2])
    axis.set(xlabel='n', title='Odd component of x[n]')
    fig.suptitle('Even and odd component of the signal')
    return fig


@app.route('/even_odd.png')
def evenOdd():
    fig = evenOdd_plot()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def evenOdd_plot():
    g = lambda x: sin(2 * 3.14 / 10 * x)
    data = even_odd(g, -5, 5)
    fig = Figure()
    axis = fig.add_subplot(1, 2, 1)
    axis.stem(data[0], data[1])
    axis.set(xlabel='n', ylabel='x[n]')
    axis = fig.add_subplot(1, 2, 2)
    axis.stem(data[0], data[2])
    axis.set(xlabel='n', ylabel='x[-n]')
    fig.suptitle('Signal x[n] & x[-n]')
    return fig


@app.route('/linearity.png')
def linearity():
    fig = linear_plot()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def linear_plot():
    f = lambda x: 2 * x
    x1 = lambda x: x
    x2 = lambda x: 2 * x
    data = linear(f, x1, x2, 0, 4)
    fig = Figure()
    axis = fig.add_subplot(1, 2, 1)
    axis.stem(data[0], data[1])
    axis.set(xlabel='n', ylabel='Output responses', title='y1[n] + y2[n]')
    axis = fig.add_subplot(1, 2, 2)
    axis.stem(data[0], data[2])
    axis.set(xlabel='n', title='y3[n]')
    fig.suptitle('Stem plots of the responses')
    return fig


@app.route('/timeVariant.png')
def timeVariant():
    fig = time_plot()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

# this block of codes does not work inside a function
# for some mysterious reasons....
funcF = 'x(t)**2'
funcG = funcF.replace('(t)', '(t-k)')
k = random.randint(-10, 10)
x = lambda t: t
f = lambda t: eval(funcF)
g = lambda t: eval(funcG)

def time_plot():
    # funcF = 'x(t)**2'
    # funcG = funcF.replace('(t)', '(t-k)')
    # k = random.randint(-10, 10)
    # x = lambda t: t
    # f = lambda t: eval(funcF)
    # g = lambda t: eval(funcG)
    data = time_invariant(f, g, x, k, -2, 4)
    fig = Figure()
    axis = fig.add_subplot(1, 2, 1)
    axis.stem(data[0], data[1])
    axis.set(xlabel='n', ylabel='Output responses', title='T{x[n-k]}')
    axis.grid()
    axis = fig.add_subplot(1, 2, 2)
    axis.stem(data[0], data[2])
    axis.set(xlabel='n', title='y[n-k]')
    axis.grid()
    return fig

if __name__ == '__main__':
    app.run(debug=True)