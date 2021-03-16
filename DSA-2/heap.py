list=[12,7,4,49]
i=len(list)-1
print(i)
k=int((i-1)/2)
print(k)
# print(k)
# j=list[k]
# z=list[p]
# print(j,z)
if list[k] < list [i]:
    # a, b = b, a
    list[i],list[k]=list[k],list[i]
    print(list)
i=k
print(i)
    
