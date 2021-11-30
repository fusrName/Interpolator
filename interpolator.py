from itertools import product
from fractions import Fraction

def polydiv(p, r):
    res = p[:]
    n = len(res)
    for i in range(n - 2, -1, -1):
        res[i] += r * res[i + 1]
    assert res[0] == 0
    res.pop(0)
    return res

def polyprod(rs):
    n = len(rs)
    allprod = [Fraction()] * (n + 1)
    allprod[0] = Fraction(1)
    for k, r in enumerate(rs):
        # multiply (-r + x) in place
        for i in range(k, -1, -1):
            allprod[i + 1] += allprod[i]
            allprod[i] *= -r
    return allprod

def build_polynomials(rs):
    allprod = polyprod(rs)
    return [polydiv(allprod, r) for r in rs]

def build_coefficients(rs):
    n = len(rs)
    res = [Fraction()] * n
    for i, ri in enumerate(rs):
        c = Fraction(1)
        for j, rj in enumerate(rs):
            if i != j:
                c /= ri - rj
        res[i] = c
    return res

def add_to_vec(ps, c, a):
    # a += prod(ps) * c
    idx = 0
    stack = []
    n = len(ps)
    # dfs params: d, i, c
    d = 0
    i = 0
    while True:
        if d < n and i < len(ps[d]):
            stack.append((i, c))
            c *= ps[d][i]
            d += 1
            i = 0
        else:
            if d == n:
                a[idx] += c
                idx += 1
            # return
            if not d:
                break
            d -= 1
            i, c = stack.pop()
            # next for-loop
            i += 1
    return

def interpolate(f, coordinates):
    coordinates = list(map(list, coordinates))
    # check coordinate distinctiveness
    for i, rs in enumerate(coordinates):
        if len(set(rs)) != len(rs):
            raise Exception(f'Values along {i}-th axis are not distict.')
    dim = tuple(map(len, coordinates))
    polys = [build_polynomials(rs) for rs in coordinates]
    coeffs = [build_coefficients(rs) for rs in coordinates]
    size = 1
    for d in dim:
        size *= d
    d = [Fraction()] * size
    for point_indices in product(*map(range, dim)):
        c = f(*(rs[i] for i, rs in zip(point_indices, coordinates)))
        for i, cs in zip(point_indices, coeffs):
            c *= cs[i]
        ps = tuple(p[i] for i, p in zip(point_indices, polys))
        add_to_vec(ps, c, d)
    return d


def interpolation_printer(a, dim, varnames=None):
    n = len(dim)
    if varnames is None:
        if len(dim) > 26:
            raise Exception("'varnames' must be provided when len(dim) > 26.")
        varnames = ''.join(chr(ord('a') + i) for i in range(len(dim)))
    if len(varnames) < len(dim):
        raise Exception("Number of var names is insufficient.")
    
    terms = []
    idx = 0
    for es in product(*map(range, dim)):
        c = a[idx]
        idx += 1
        if c != 0:
            terms.append((c, es))
    res = []
    for c, es in sorted(terms, key=lambda e: (sum(e[1]), e[1]), reverse=True):
        if c < 0:
            res.append('-')
            c = -c
        elif res:
            res.append('+')
        vs = []
        for x, e in zip(varnames, es):
            vs += (x for _ in range(e))
        v = '*'.join(vs)
        if not v:
            res.append(str(c))
            continue
        res.append(v)
        if c.numerator != 1:
            res.append('*')
            res.append(str(c.numerator))
        if c.denominator != 1:
            res.append('/')
            res.append(str(c.denominator))
    if not res:
        res.append('0')
    print(''.join(res))
