class newNode:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None

def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left 
    return d
def Depth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.right 
    return d 

def chill(node):
    d= calculateDepth(node) + Depth(node)
    if d%2==0:
        print("not full binary tree")
    else:
        print("full binary tree")

root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.left.left.left = newNode(40)    

# calculateDepth(root)
# print()
# Depth(root)
print(chill(root))