import os

value=input("input your data = ")
list=[None]*10
j=10
ok=0
for i in value:
    b=ord(i)
    # print(b)
    ok=ok+b
chill=ok%j
print(chill)

#def insert(self,chill,value):
    #hash_key=chill
    #list[hash_key]=value
    #return list
#print(insert(chill,value))


save_path="/media/rahman/E6D9-6CB0"
name_of_file = input("What is the name of the file: ")
file_extension=input("give file extension: ")
completeName = os.path.join(save_path, name_of_file+file_extension)
list=[None]*10
j=10
ok=0
for i in completeName:
    b=ord(i)
    # print(b)
    ok=ok+b
chill=ok%j
print(chill)