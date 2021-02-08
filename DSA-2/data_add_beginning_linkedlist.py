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
            while n is not None:
                print(n.data,"--->",end="")
                n=n.ref

    def beginning_add(self,data):
        add_data=node(data)
        add_data.ref=self.head
        self.head=add_data

    def end_add(self,data):
        new_node=node(data)
        if self.head == None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_middle(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("node is not here ")
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def delete_begin(self):
        if self.head== None:
            print("ll is emipty")
        else:
            self.head=self.head.ref

obj=linkedlist()
obj.beginning_add(12)
obj.beginning_add(14)
obj.beginning_add(14)
obj.beginning_add(16)
obj.end_add("Rahman Bhuiyan")
obj.add_middle(89,14)
obj.delete_begin()
obj.link_node()