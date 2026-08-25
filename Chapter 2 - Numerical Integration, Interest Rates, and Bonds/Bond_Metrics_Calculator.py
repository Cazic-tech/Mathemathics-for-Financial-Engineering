import math

# Pricing bond and metrics based on given yield

#INPUTS#

T = 14/12 #Bond maturity in years
n = 5 #Number of Cash Flows
t_cf = [2/12,5/12,8/12,11/12,14/12]  #timing of cash-flows, annual base
v_cf = [2,2,2,2,102]  #value of cashflows 
face_value = 100
y = 0.07 #yield of the bond

def bond_metrics(n,t_cf,v_cf,y):

    bond = 0
    duration = 0
    convexity = 0

    for i in range(n):
        t = t_cf[i]
        v = v_cf[i]
        discount_factor = math.exp(-y*t)
        bond += v * discount_factor
        duration += t*v*discount_factor
        convexity += t**2 *v*discount_factor

    duration = duration/bond
    convexity = convexity/bond

    return bond, duration, convexity

metrics = bond_metrics(n,t_cf,v_cf,y)

print("Bond Price:",metrics[0])
print("Bond Duration:",metrics[1])
print("Bond Convexity:",metrics[-1])
