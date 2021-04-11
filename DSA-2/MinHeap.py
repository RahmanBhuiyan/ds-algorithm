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
    def hasleftchild(self,index):
        return self.Rleftchild(index) < self.size
    def hasrightchild(self,index):
        return self.RrightChild(index) < self.size
    def aSwap(self,index):
        if self.hasparent(index) and self.storage[self.leftchild(index)] > self.storage[self.Rightchild(index)]:
            self.storage[self.leftchild(index)],self.storage[self.Rightchild(index)]=self.storage[self.Rightchild(index)],self.storage[self.leftchild(index)]
    def Rleftchild (self,index):
        return index*2+1
    def RrightChild(self,index):
        return index*2+2
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
    def remove(self):
        if (self.size==0):
            return "heap is empty"
        data=self.storage[0]
        self.storage[0]=self.storage[self.size-1]
        self.size-=1
        # return self.storage.remove(self.storage[self.size])
        # self.storage.remove([self.size-=1])
        self.heapdown()
        return data  
    def heapdown(self):
        index=0
        while self.hasleftchild(index):
            child=self.Rleftchild(index)
            if self.hasrightchild(index) and (self.storage[self.RrightChild(index)] < self.storage[self.Rleftchild(index)]):
                child=self.RrightChild(index)
            if self.storage[index] < self.storage[child]  :
                #parent < child 
                break
            else:
                self.swap(index,child)
            index=child
        self.storage.remove(self.storage[self.size])


obj=MinHeap(10)
obj.insert(0)
obj.insert(5)
obj.insert(10)
obj.insert(20)
obj.insert(8)
obj.insert(15)
obj.insert(30)
print(obj.remove())
print(obj.remove())
print(obj.size)
print(obj.storage)