from sage.all import *

p,z=var('p','z')
s=solve((sec((p+z)/2))**4+(sec((p-z)/2))**4,p)
l=latex(s)
print(l)
