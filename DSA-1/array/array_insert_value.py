def array(u_indx,u_data):
    list=[20,30,40,50,None]
    if list[u_indx] is not None:
        lant=len(list)
        index=u_indx
        while index < lant:
            index=index+1
#            lant=lant-1
            list[lant]=list[lant-1]
    list[u_indx]=u_data   
    return list
print(array(2, 100))
            
        