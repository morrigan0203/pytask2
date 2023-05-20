import math
import cmath

a = 5
b = -10
c = 400
x1 = None
x2 = None
D = (b ** 2 - 4 * a * c)
x1 = ( - b + cmath.sqrt(D)) / ( 2 * a )
x2 = ( - b - cmath.sqrt(D)) / ( 2 * a )
print(x1, x2)
if isinstance(x1, complex):
    print(True)
if isinstance(x2, complex):
    print(True)

