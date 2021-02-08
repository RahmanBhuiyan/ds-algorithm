# q=0.1+0.2
# c=0.30000000000000004
# if(q==c):
#     print(1)
# else:
#     print(2)
# i=0.1+0.2
# print(i)
# print(round(2.006,1))


a=int(input("input your number = "))
b=int(input("input your number = "))
c=int(input("input your number = "))
def large_number(a,b,c):
    if a>b and a>c:
    #a greater than b and a greater than c ,a is large number 
        print(a)
    elif b>a and b>c:
    #b greater than a and b greater than c ,b is large number
        print(b)
    else:
        print(c)
    #if this two condition are false c is the large number  
print(large_number(a,b,c))