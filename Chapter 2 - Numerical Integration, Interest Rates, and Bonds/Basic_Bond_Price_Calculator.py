import math
import numpy as np

# INPUTS
 # this calculator is only for annual paying bonds
 
n = 4  #number of cash flows
coupon = 50
face_value = 1000
# t_cf = [1,2,3,4] #vector of cash flow dates
#v_cf = [50,50,50,1050] #vector of cash flows

t_cf=[]
v_cf=[]

for i in range(1,n+1):
    t_cf.append(i)

    if i == n:
        v_cf.append(coupon+face_value)
    else:
        v_cf.append(coupon)

rates = {1:0.04, 2:0.045, 3:0.05, 4:0.055}

def r_zero(t):
    return  rates[t] #zero rate corresponding to time t

# Bond Price

def bond_price(n,t_cf,v_cf,r_zero):

    bond = 0

    for i in range(n):
        t = t_cf[i]
        v = v_cf[i]
        discount_factor = math.exp(-rates[t]*t)
        bond += v * discount_factor

    return bond

print(bond_price(n,t_cf,v_cf,r_zero))
