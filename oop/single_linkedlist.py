class Node :
    def __init__ (self,data):
        self.data=data
        self.next=None
class linkedlist(Node):
    def __init__(self):
        # super().__init__(data)
        self.head=None
    def print_link(self):
        if self.head == None :
            print("linked list is empty")
        else:
            n=self.head
            while n is not none:
                print(n.data)
                n=n.next
obj=linkedlist()
print(obj)
obj. print_link()
