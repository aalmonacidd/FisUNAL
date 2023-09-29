from sage.all import *

A=matrix([[2,1,0],[1,2,0],[0,0,3]])
vals=A.eigenvalues()
vecs=A.eigenvectors_left()
print(A)
print(vals)
print(vecs)
