class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        self.pre=None
class double_linkedlist:
    def __init__(self):
        self.head=None
    def link_f_node(self):
        if self.head == None:
            print("linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end="")
                n=n.ref
    def link_b_node(self):
        print()
        if self.head is None:
            print("linkedlist is empty")
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            while n is not None:
                print(n.data,"--->",end="")
                n=n.pre
    def add_beggin(self,data):
        new_node=node(data) 
        if self.head is None:
            self.head=new_node
        else:
            new_node.ref=self.head
            self.head.pre=new_node
            self.head=new_node

    def delate(self):
        if self.head is None:
            print("ther is not any node")
        if self.head.ref is None:
            self.head=None
            print("list is empty there is not any node ")
        else:
            self.head=self.head.ref
            self.head.pre=None

    # def insert_emipty(self,data):
    #     if self.head is None:
    #         new_node=node(data)
    #         self.head=new_node
    #     else:
    #         print('linkedlist is not empty')

    # def beginning_add(self,data):
    #     add_data=node(data)
    #     add_data.ref=self.head
    #     self.head=add_data
obj=double_linkedlist()
# obj.add_beggin(12)
obj.add_beggin(30)
obj.add_beggin(90)
obj.add_beggin(300)
obj.delate()
obj.delate()
obj.link_f_node()
obj.link_b_node()