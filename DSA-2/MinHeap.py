class MinHeap:
    def __init__(self,capacity):
        self.storage=[None]*capacity
        self.capacity=capacity
        self.size=0
    def parent(self,index):
        return int((index -1)/2)
    def hasparent(self,index):
        return self.parent(index)>=0
    def getParent(self,index):
        return self.storage[self.parent(index)]
    def storage_full(self):
        return self.storage==self.size
    def swap(self,index1,index2):
        temp=self.storage[index1]
        self.storage[index1]=self.storage[index2]
        self.storage[index2]=temp
    def leftchild(self,index):
        return 2*self.parent(index)+1
    def Rightchild(self,index):
        return 2*self.parent(index)+2
    def aSwap(self,index):
        if self.hasparent(index) and self.storage[self.leftchild(index)] > self.storage[self.Rightchild(index)]:
            self.storage[self.leftchild(index)],self.storage[self.Rightchild(index)]=self.storage[self.Rightchild(index)],self.storage[self.leftchild(index)]

    def insert(self,data):
        if(self.storage_full()):
            return "Heap is full"
        self.storage[self.size]=data
        #insert data in the list
        self.size+=1
        self.HeapUp()
    def HeapUp(self):
        index=self.size -1
        while (self.hasparent(index)and (self.getParent(index)>self.storage[index])):
            self.swap(self.parent(index),index)
            index=self.parent(index)
            self.aSwap(index)

obj=MinHeap(10)
obj.insert(3)
obj.insert(9)
obj.insert(2)
obj.insert(1)
obj.insert(4)
obj.insert(5)
print(obj.storage)