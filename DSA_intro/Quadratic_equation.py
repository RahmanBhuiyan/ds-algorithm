import math
def quadratic_equation():
    a=int(input("input number = "))
    b=int(input("input number = "))
    c=int(input("input number = "))
    z=(b**2-4*a*c)**.5
    x=-b+z
    m=x/2*a
    #square root math(square root y=y**1/2=y**0.5)
    #25**0.5=5(y=25)
    y=-b-z
    n=y/2*a
    return m,n
print(quadratic_equation())




# print(round(2.467))
# print(round(1.065,2))


