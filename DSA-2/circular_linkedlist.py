class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def link_node(self):
        if self.head == None:
            print("linkedlist is empty")
        else:
            n=self.head
            while n :
                print(n.data,"--->",end="")
                n=n.ref
                if n==self.head:
                    break
    # def add_beggin(self,data):
    #     new_node=node(data)
    #     new_node.ref=self.head
    def add_end(self,data):
        if self.head is None:
        #when there is any node in the list this is the first node of the list 
            self.head=node(data)
            #i creat a object with self.head in this way i fixed my first head node
            self.head.ref=self.head
            #this is way my first node work in the circule 
        else:
            new_node=node(data)
            n=self.head
            while n.ref is not self.head:
                n=n.ref
            n.ref=new_node
            new_node.ref=self.head
    # def delete_begin(self):
    #     if self.head== None:
    #         print("ll is emipty")
    #     else:
    #         self.head=self.head.ref
obj=linkedlist()
obj.add_end(12)
obj.add_end(13)
obj.link_node()