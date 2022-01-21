import math
a=int(input("input your number: "))
b=int(input("input your number: "))
c=int(input("input your number: "))

d=(b**2)-4*(a*c)
if d>0:
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    
    print("root are real and unequal and are : ",x1,x2)
    
elif d==0:
    x=-b/(2*a)
    print("root are real and unequal and are : ", x)
    
else:
    print("the roots are imaginary ")
    
    
