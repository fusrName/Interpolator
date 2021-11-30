from interpolator import interpolate, interpolation_printer


def f(x, y, z):
    return x*x*y*3 + x*x*2 + x*y*6 - x*13 - y*235 - 3351

xs = [2,3,5]
ys = [0,1]
zs = [3]
ps = (xs, ys, zs)
res = interpolate(f, ps)
interpolation_printer(res, tuple(map(len, ps)), 'xyz')


def g(x):
    return sum(range(x + 1))  # equals to x(x+1)/2

res = interpolate(g, (range(10),))
interpolation_printer(res, (10,))