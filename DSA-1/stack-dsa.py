class stack:
    def __init__(self):
        self.hdd=[]

    def push (self,add):
        self.hdd.append(add)
        return self.hdd
    def pop(self):
        self.hdd.pop(-1)
        return self.hdd
    def storaze (self):
        size=len(self.hdd)
        if size==10:
            print("storaze is full")
        else:
            print("stpraze is not full add your data")
dh=stack()
print(dh.push(1))
print(dh.push("hello"))
print(dh.pop())
print(dh.storaze())


# class stack:
#     hdd=[]
#     def push(self, hdd):
#         hdd.append()
#         size=len(add)
#         self.hdd=hdd
#         self.size=size
#         return self.hdd
#     # def storaze(self):
#     #     if self.size==100:
#     #         print("storaze is full")
#     #     else:
#     #         print("storze is not full add data")
#     # def pop(self,hdd):
#     #     hdd.pop(-1)
#     #     self.delate=hdd
#     #     return self.delate
# dh=stack("13")
# print(dh.push())        