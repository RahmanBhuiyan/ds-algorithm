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
        return chill
    def insert (self,key,val):
        ok=self.hash_function(key)
        self.list[ok]=val
    def get (self,key):
        ok=self.hash_function(key)
        return self.list[ok]
    def delate(self,key):
        # delate iteam in the hashtable
        ok=self.hash_function(key)
        self.list[ok]=None
t=hashtable()
t.insert("rahman",450)
t.insert("bhuiyan",450)
t.insert("error 4044","01869019351")
print(t.get("rahman"))
print(t.get("error 4044"))
print(t.list)

'''
#nonetype error how to solve 

# def demo():
# 	print(3+4)
# print('printed fucntion return none\n', demo())

# # n = demo()+3
# # print(n) #this will produce error.


# def demo1():
# 	return 3+4
# print('returned function returns the value\n',demo1())

# n1 = demo1()+3
# print(n1)
'''