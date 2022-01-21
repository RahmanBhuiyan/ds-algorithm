import os
class hashtable:
    def __init__(self):
        self.max=10
        self.list=[[]]*self.max
    def hash_function(self,key):
        ok=0
        for i in key:
            b=ord(i)
            ok=ok+b
        chill=ok%self.max
    def creat_file(name_of_file = input("What is the name of the file: ")):
        save_path="/media/rahman/E6D9-6CB0"
        completeName = os.path.join(save_path, name_of_file)
        file1 = open(completeName, "w")
        return file1
    def insert (self,key,vel):
        ok=self.hash_function(key)
        self.list[ok]=self.creat_file(vel)
    def get (self,key):
        ok=self.hash_function(key)
        return self.list[ok]
    def delate(self,key):
        # delate iteam in the hashtable
        ok=self.hash_function(key)
        self.list[ok]=None
t=hashtable()
#t.insert("rahman",450)
#t.insert("bhuiyan",450)
#t.insert("error 4044","01869019351")
#print(t.get("rahman"))
#print(t.get("error 4044"))
#print(t.list)
t.creat_file()

