
import math
import numpy as np


# INPUTS #

a = 0 #left endpoint
b = 3  #right endpoint
n = 4 #number of partitions interval
tol = 1e-8  # prescribed tolerance
def f(x):
    return 0.05/(1+math.exp(-(1+x)**2))  #routine evaluating f(x)


# MIDPOINT RULE

def midpoint_rule(a,b,n,f):
    h = (b-a)/n
    midpoint = 0

    for i in range(1,n+1):
        x_mid = a+(i-0.5)*h
        midpoint += h*f(x_mid)  #shortcut for = midpoint+ h*f(x_mid)

    return midpoint


# Trapezoidal Rule

def trapezoidal_rule(a,b,n,f):
    h = (b-a)/n
    trapezoidal = f(a)+f(b)

    for i in range(1,n):
        x_i = a + i*h
        trapezoidal += 2*f(x_i)

    trapezoidal *= h/2

    return trapezoidal


#    def trap_rule(a,b,n,f):      #alternative code using the trap area function
#        h = (b-a)/n
#        trap = 0
#
#        for i in range(1,n+1):
#            x1 = a+(i-1)*h
#            x2 = a+i*h
#            trap += h*(f(x1)+f(x2))/2
#
#        return trap
#
#    print(trap_rule(a,b,n,f))


# Simpson's Rule

def simpson_rule(a,b,n,f):

    h = (b-a)/n
    simpson = h*(f(a)+f(b))/6

    #Partition points
    for i in range(1,n):
        a_1 = a + i*h
        simpson += h*f(a_1)/3

    #Midpoints
    for i in range(1,n+1):
        x_i = a + (i-0.5)*h
        simpson += 2*h*f(x_i)/3

    return simpson



# Approximatation with a given tolerance

def adaptive_integration(rule,a,b,f,tol):

    n=1
    old = rule(a,b,n,f)

    n =2
    new = rule(a,b,n,f)

    while abs(new-old)>tol:
        old=new
        n *= 2
        new = rule(a,b,n,f)

    return new, n

midpoint, n_mid = adaptive_integration(midpoint_rule, a, b, f, tol)
trapezoid, n_trap = adaptive_integration(trapezoidal_rule, a, b, f, tol)
simpson, n_simp = adaptive_integration(simpson_rule, a, b, f, tol)


if __name__=="__main__":
    print("n:", n)
    print("Midpoint Rule (Manual):",midpoint_rule(a,b,n,f))
    print("Trapezoidal Rule (Manual):",trapezoidal_rule(a,b,n,f))
    print("Simpson's Rule (Manual):",simpson_rule(a,b,n,f))
    print()
    print("="*30)
    print()
    print("Adaptive Integration with Especified Tolerance Value")
    print()
    print("Midpoint:", midpoint, "n=", n_mid)
    print("Trapezoidal:", trapezoid, "n=", n_trap)
    print("Simpson:", simpson, "n=", n_simp)
        




