from sage.all import *

def metrica(d,eq1,eq2,u,v):
    g_=d*matrix([[eq1.diff(u),eq2.diff(u)],[eq1.diff(v),eq2.diff(v)]])**2
    return g_
x,t,p,z=var('x','t','p','z')
eqp=tan((1/2)*(p+z))
eqm=tan((1/2)*(p-z))
d_=matrix([[1,0],[0,1]])
print(eqp.diff(p).full_simplify())

