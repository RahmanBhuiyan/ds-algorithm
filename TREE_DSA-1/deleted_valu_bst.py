class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

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
    def deleted(self,data):
        if data < self.data:
            if self.left:
                self.left=self.left.deleted(data)
        elif data > self.data:
            if self.right:
                self.right=self.right.deleted(data)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_data=self.right.min()
            self.data=min_data
            self.right=self.right.deleted(self.data)

        return self





def build_tree(elements):
    root=Node(elements[0])

    for i in range (1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=="__main__":
    numbers=[34,89,10,9,7,12]
    number_tree=build_tree(numbers)
    number_tree.deleted(7)
    print(number_tree.inoder_traversal())