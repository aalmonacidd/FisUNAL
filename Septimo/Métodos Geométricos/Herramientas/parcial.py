from sage.all import *

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')
    
def velocidad(curva,t):
    velocidad_={'x.':curva[0].diff(t),'y.':curva[1].diff(t), 'z.':curva[2].diff(t)}
    return velocidad_
def aceleracion(curva,t):
    acele_={'x.':curva[0].diff(t,2),'y.':curva[1].diff(t,2), 'z.':curva[2].diff(t,2)}
    return acele_
def norma(vector):
    norma_=sqrt(vector[0]**2+vector[1]**2+vector[2]**2)
    return norma_
def normalizado(vector):
    norma_=sqrt(vector[0]**2+vector[1]**2+vector[2]**2)  
    normaliz_=[vector[0]/norma(vector),vector[1]/norma(vector),vector[2]/norma(vector)]
    return normaliz_
def punto(v,w):
    vr_=[v[0]*w[0],v[1]*w[1],v[2]*w[2]]
    return vr_
def rd(curva,t):
    rd_=[curva[0].diff(t),curva[1].diff(t),curva[2].diff(t)]
    return rd_
def rdd(curva,t):
    rdd_=[curva[0].diff(t,2),curva[1].diff(t,2),curva[2].diff(t,2)]
    return rdd_
def rddd(curva,t):
    rddd_=[curva[0].diff(t,3),curva[1].diff(t,3),curva[2].diff(t,3)]
    return rddd_
t= var('t')
eq=[(1/2)-t**2,t*sqrt(1-t**2),t]
print('Curva parametrizada')
print(eq)
print('Calculo de velocidad y aceleracion')
print(velocidad(eq,t))
print(aceleracion(eq,t))
rt=vector(rd(eq,t))
rtt=vector(rdd(eq,t))
print('Calculo de Kappa')
kappa=norma(rt.cross_product(rtt))/(norma(rt))**3
k=kappa.full_simplify().trig_expand()
print(k)
print(latex(k))
print('Cálculo de Chi')
rttt=vector(rddd(eq,t))
chi=-(rt.dot_product(rtt.cross_product(rttt)))/(norma(rt.cross_product(rtt)))**2
c=chi.full_simplify().trig_expand()
print(c)
print(latex(c))

