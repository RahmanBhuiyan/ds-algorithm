number=int(input("input your number = "))
a=0 
b=1
print(a)
print(b)

# print(end="")
for i in range(number):
    c=a+b
    #transfer value a to b and b to c
    a=b
    b=c
    print(c) 
    
# z=1
# f(n)=z+z+n+1
#     =2*1+n+1
#     =3+n
#     =n 
#     o(n)
      