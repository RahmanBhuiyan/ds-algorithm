class queue:
    def __init__(self):
        self.hdd=[]
    def enqueue (self,add):
        self.hdd.append(add)
        return self.hdd
    def dequeue (self):
        self.hdd.pop(0)
        return self.hdd
    def storaze (self):
        size=len(self.hdd)
        if size==4:
            print("storaze is full")
        else:
            print("stpraze is not full add your data")
    # def peek (self):
    #     size=len(self.hdd)
    #     if size==0:
    #         return size
dh=queue()
print(dh.enqueue(12))
print(dh.enqueue(14))
print(dh.enqueue(16))
print(dh.enqueue(16))
print(dh.dequeue())
print(dh.storaze())
