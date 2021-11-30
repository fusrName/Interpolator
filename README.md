# Interpolator
predicts the original polynomial by applying Lagrange interpolation in a multidimensional way.
It takes a function to be predicted and lists of coordinates, where i-th list contains coordinates along i-th axis.
The set of sample points used for prediction is the *product* set of them.
Not packaged and everything just put inside main.py because of myyyyy.

## Methods
```python
interpolate(f, ps)
```
returns a list which represents a polynomial. Time complexity Ω(Π<sub>xs∈ps</sub> len(xs)<sup>2</sup>), where the cost of Fraction arithmetics is not taken into consideration.
```python
interpolation_printer(interpolation, dim, varnames=None)
```
takes the result above and prints the polynomial. Provide `tuple(map(len, ps))` for dim. When varnames specified, they will be used for variable names, while *a, b, c, ...* are used by default.

## Example
```python
def f(x, y, z):
    return x*x*y*3 + x*x*2 + x*y*6 - x*13 - y*235 - 3351

xs = [2,3,5]
ys = [0,1]
zs = [3]
ps = (xs, ys, zs)
res = interpolate(f, ps)
interpolation_printer(res, tuple(map(len, ps)), 'xyz')  # outputs x*x*y*3+x*x*2+x*y*6-x*13-y*235-3351
```
predicts *f* using values f(2,0,3), f(2,1,3), f(3,0,3), f(3,1,3), f(5,0,3), and f(5,1,3).
Since [2,3,5], [0,1], [3] are of lengh 3, 2, 1 respectively, the terms of the form c<sub>ijk</sub>x<sup>i</sup>y<sup>j</sup>z<sup>k</sup> s.t. 0 &le; i &lt; 3, 0 &le; j &lt; 2, 0 &le; k &lt; 1 are considered.
c<sub>ijk</sub> is stored in res[i * 2 * 1 + j * 1 + k].