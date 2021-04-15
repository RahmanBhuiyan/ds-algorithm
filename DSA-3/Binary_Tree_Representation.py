class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data

    def preorder(self):
        print(self.val,end="")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val,end="")
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val,end="")
        if self.right:
            self.right.inorder()
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.preorder()
print("\nIn order Traversal: ", end="")
root.inorder()
print("\nPost order Traversal: ", end="")
root.postorder()
