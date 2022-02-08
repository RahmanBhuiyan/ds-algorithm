def pos(str1,str2):
    #convert str1 and str2 in string
    list_str1=list(str1)
    list_str2=list(str2)
    #use loop list_str1 and list_str2 both of them 
    for strings in list_str2,list_str1:
        #compare list_str1 and list_str2 
        if strings in strings :
            return "Yes"
        else:
            return "No"
print(pos("donut","Nabucodonosor"))
