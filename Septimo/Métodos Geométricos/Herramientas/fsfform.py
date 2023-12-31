from sage.all import *

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f'{key}: {value}')

def calc_first_derivatives(surface ):
    first_derivative_ = surface.natural_frame()
    first_derivative = {'u': first_derivative_[1], 'v': first_derivative_[1]}
    return first_derivative
    

def calc_second_derivatives(surface ):
    first_derivative = calc_first_derivatives(surface)
    second_derivative = {'uu': derivative(first_derivative['u'],u),
                         'uv': derivative(first_derivative['u'],v),
                         'vv': derivative(first_derivative['v'],v),
                         'vu': derivative(first_derivative['v'],u),}
    return second_derivative

def dot_products(surface ):
    first_derivative = calc_first_derivatives(surface)
    second_derivative = calc_second_derivative(surface)
    normal = surface.normal_vector()

u,v,a,b = var('u,v,a,b',domain='real')

eq = [(2-v*sin(u/2))*cos(u), (2-v*sin(u/2))*sin(u), v*cos(u/2)]
surface = ParametrizedSurface3D(eq, [u,v])

print(f'{surface}\n')

print('First derivatives: ')
print_dict(calc_first_derivatives(surface))
print('\n')

print('Second derivatives:')
print_dict(calc_second_derivatives(surface))
print('\n')

print(f'Normal vector: {surface.normal_vector()} ')
print('\n')
print(f'Normalized normal vector: {surface.normal_vector(normalized=True)}')
print('\n')

print('First fundamental form:')
print_dict(surface.first_fundamental_form_coefficients())
print('\n')

print('Second fundamental form:')
print_dict(surface.second_fundamental_form_coefficients())
print('\n')

print(surface.normal_vector().dot_product(calc_second_derivatives(surface)['uu']).full_simplify())
