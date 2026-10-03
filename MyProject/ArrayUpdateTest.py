from numpy import *

ar1 = array([2, 3, 1, 4, 5])
print(id(ar1))
ar2 = ar1
ar1 = ar1 + 5
print(id(ar1))
print(id(ar2))
print(ar1)
print(ar2)
