def f(x):
    return g(x, 1)


def g(x, acc):
    if x == 0:
        return acc
    else:
        return g(x - 1, acc * x)
