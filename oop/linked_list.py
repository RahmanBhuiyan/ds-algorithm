# class linked_list:
#     def __init__ (self,item):
#         self.item=item
#         self.head=None
#     def insert(self):
#         d=id(self.item)
#         self.head=d
#         if self.head != None:
#             return self.item
# obj=linked_list(5)
# obj=linked_list(6)
# print(obj.insert())

# class node:
#     def __init__ (self):
#         self.next=None
#     def node_link(self,data):
#         self.data=data
#         self.next=None
# class linkedlist(node):
#     def __init__(self):
#         node.__init__(self)
#         self.head=None
#     def link(self):
#         if self.head==None:
#             print("list is empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data)
#                 n=n.next
# obj=linkedlist()
# chill=node()
# chill.node_link(12)

class Node :
    def __init__ (self,data,next):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def link_in_the_list(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert (self):
        if self.head is None:
            print("empty")
        itr=self.head
        chill=""
        while itr:
            chill==str(itr.data)
            itr=itr.next
        print(chill)

if __name__=="__main__":
    obj=linkedlist()
    obj.link_in_the_list(12)
    obj.link_in_the_list(14)
    obj.insert()


        


