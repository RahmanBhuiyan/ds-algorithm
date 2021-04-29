class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data:
            return
        if data <self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Node(data)
    def inoder_traversal(self):
        list=[]
        #visit left tree first
        if self.left:
            list +=self.left.inoder_traversal()
        #visit root node
        list.append(self.data)

        #visit right tree

        if self.right:
            list+=self.right.inoder_traversal()

        return list
    def preorder_traversal(self):
        list=[]

        #visit root node
        list.append(self.data)

        #visit left tree first
        if self.left:
            list +=self.left.inoder_traversal()

        #visit right tree

        if self.right:
            list+=self.right.inoder_traversal()

        return list
    def postorder_traversal(self):
        list=[]

        #visit left tree first
        if self.left:
            list +=self.left.inoder_traversal()

        #visit right tree

        if self.right:
            list+=self.right.inoder_traversal()
        
        #visit root node
        list.append(self.data)

        return list
    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def search(self,data):
        if data==self.data:
            return True
        #if data is less than root go to left subtree      
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        #if data is grater than root go to right subtree      
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

def build_tree(elements):
    root=Node(elements[0])

    for i in range (1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=="__main__":
    numbers=[12,34,89,10,9,7,34,12]
    number_tree=build_tree(numbers)
    print(number_tree.inoder_traversal())
    print(number_tree.preorder_traversal())
    print(number_tree.postorder_traversal())
    print(number_tree.min())
    print(number_tree.max())
    print(number_tree.search(100))