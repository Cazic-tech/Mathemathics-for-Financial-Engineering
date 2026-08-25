# Bond Price given the Instantaneous rate curve based on the example of the book "A Primer for the Mathemathics of Financial Engineering"
import math
from Calculator_Numerical_Integration_Methods import adaptive_integration, simpson_rule

#INPUTS#

face_value = 100
coupon_rate = 0.05
pmt_per_year = 1
maturity_months = 36 #months
tol = 1e-10

def r_z(t):  #zero rate curve
    return 0.0525 + math.log(1+2*t)/200

def r_inst(t):  #instantaneus rate curve
    return 0.05/(1+math.exp(-(1+t)**2))


#MODEL#

coupon = face_value * coupon_rate/pmt_per_year
n = math.ceil(maturity_months/(12/pmt_per_year))
first_payment_month = maturity_months - (n-1)*(12/pmt_per_year)

v_cf = []
t_cf = []

for i in range(1, n+1):

    payment_month = first_payment_month + (i-1)*(12/pmt_per_year)
    t_cf.append(payment_month/12)
    
    if i == n:
        v_cf.append(coupon + face_value)
    else:
        v_cf.append(coupon)


def bond_price_zero(t_cf,v_cf,n):
    bond = 0

    for i in range(n):
        t = t_cf[i]
        v = v_cf[i]

        df = math.exp(-r_z(t)*t)
        bond += v * df
    return bond

print("Bond Price Zero Rate Curve:",bond_price_zero(t_cf,v_cf,n))

def bond_price_inst(t_cf,v_cf,n,rule,tol,f):
    bond = 0

    for i in range(n):
        t = t_cf[i]
        v = v_cf[i]

        integral, n_used = adaptive_integration(rule,0,t,f,tol)
        df = math.exp(-integral)
        bond += v*df

    return bond

print("Bond Price Instantaneous Rate Curve:",bond_price_inst(t_cf,v_cf,n,simpson_rule,tol,r_inst))

