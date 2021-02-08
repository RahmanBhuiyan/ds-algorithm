class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
class linkedlist(Node):
    def __init__(self,data):
        Node.__init__(self,data) 
        self.head=None
    def link(self):
        self.head=self.data
        while self.data :
            print(self.data)
        self.pointer=self.head
obj=linkedlist("12")
obj.link()


