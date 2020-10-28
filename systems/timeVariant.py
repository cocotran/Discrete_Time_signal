# Definition: A system is time invariant (TI) if given
# 𝑦[𝑘] = 𝑇{𝑥[𝑘]}
# Then
# 𝑇{𝑥[𝑘 − 𝑘0]} = 𝑦[𝑘 − 𝑘0], ∀𝑥[𝑘], 𝑎𝑛𝑑 ∀𝑘0 ∈ ℤ

# Note: does not work with signal scalling e.g. y[k] = x[2t]

# parameter: system function, input x[n], interval from, interval to
def time_invariant(f, g, x, k, n_from: int, n_to: int):
    # k can take any value, for simplicity we set k to be in small range
    # input signal x[n] can be anything, for simplicity this case is used
    # define n
    n = [i for i in range(n_from, n_to + 1)]
    n_0 = [i - k for i in n]

    # # output response by input x[n-k]
    y = [f(i) for i in n_0]

    # # output response y[n-k]
    y_minus_k = [g(i) for i in n]

    isEqual = False
    for i in range(len(n)):
        if (y[i] == y_minus_k[i]):
            isEqual = True
        else:
            isEqual = False
    if isEqual:
        print('System is time invariant')
    else:
        print('System is time varying.')
    return [n, y, y_minus_k]