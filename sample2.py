from interpolator import interpolate, interpolation_printer

def g(i, j):
    k = i + j
    return k * (k + 1) // 2 + i

def f(h2, w2, bh, bw):
    h = 2 * h2 + bh
    w = 2 * w2 + bw
    d = sorted(g(i, j) for i in range(h) for j in range(w))
    c = d[len(d) // 2]
    return 6 * sum(abs(x - c) for x in d)

hs = range(1, 11)
ws = range(15, 25)
bh = range(2)
bw = range(2)
ps = (hs, ws, bh, bw)
res = interpolate(f, ps)
interpolation_printer(res, tuple(map(len, ps)), ['h2', 'w2', 'bh', 'bw'])