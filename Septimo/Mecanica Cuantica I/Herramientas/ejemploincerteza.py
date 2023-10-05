from sage.all import *

h,x_0,p_0,a,x=var('h','x_0','p_0','a','x')
f=function('f')(x)
eq=-I*h*diff(f,x)==(I*a*(x-x_0)+p_0)*f
s=desolve(eq,[f,x])
print(s)
