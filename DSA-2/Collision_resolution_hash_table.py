class hashtable:
    def __init__(self):
        self.max=100
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
        for idx,elemant in enumerate(self.list[ok]):
            if len(elemant)==2 and elemant[0]==key:
                self.list[ok][idx]=(key,val)
                break
        self.list[ok].append(key,val)
    def get (self,key):
        ok=self.hash_function(key)
        return self.list[ok]
    def delate(self,key):
        # delate iteam in the hashtable
        ok=self.hash_function(key)
        self.list[ok]=None
t=hashtable()
t.insert("rahman",450)
t.insert("error 4044","01869019351")
print(t.get("rahman"))
print(t.get("error 4044"))
print(t.list)