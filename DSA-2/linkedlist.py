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
                print(n.data)
                n=n.ref
obj=linkedlist()
obj.link_node()
