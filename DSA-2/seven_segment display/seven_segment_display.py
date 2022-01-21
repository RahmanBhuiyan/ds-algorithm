zero = '###\n# #\n# #\n# #\n###\n\n'
one = '#\n#\n#\n#\n#\n\n'
two = '###\n  #\n###\n#  \n###\n\n'
three = '###\n  #\n###\n  #\n###\n\n'
four = '# #\n# #\n###\n  #\n  #\n\n'
five = '###\n#  \n###\n  #\n###\n\n'
six = '###\n#  \n###\n# #\n###\n\n'
seven = '###\n  #\n  #\n  #\n  #\n\n'
eight = '###\n# #\n###\n# #\n###\n\n'
nine = '###\n# #\n###\n  #\n###\n\n'

def seven_segment_display(data):
    if data>=0:
        store_disply_num=""
        str_data=str(data)
        for i in range(len(str_data)):
            if str_data[i]=="0":
                store_disply_num+=zero

            if str_data[i]=="1":
                store_disply_num+=one
                
            if str_data[i]=="2":
                store_disply_num+=two
                
            if str_data[i]=="3":
                store_disply_num+=three
                
            if str_data[i]=="4":
                store_disply_num+=four

            if str_data[i]=="5":
                store_disply_num+=five
                
            if str_data[i]=="6":
                store_disply_num+=six
                
            if str_data[i]=="7":
                store_disply_num+=seven
                
            if str_data[i]=="8":
                store_disply_num+=eight          

            if str_data[i]=="9":
                store_disply_num+=nine  
        return store_disply_num
print(seven_segment_display(678), end = ' ')
