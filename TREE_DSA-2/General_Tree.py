class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child) 

    def print_tree(self):
        space="   " * self.get_level() *2
        print(space+self.data)
        if self.children:
            for child in self.children:
                child.print_tree() 

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent

        return level   

def build_product_tree():
    root=TreeNode("Electronic")

    laptop=TreeNode("laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone=TreeNode("cell phone")
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("google pixel"))
    cellphone.add_child(TreeNode("walton"))

    tv=TreeNode("tv")
    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("walton"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)



    print(cellphone.get_level())
    return root
if __name__=="__main__":
    build_product_tree()
    root=build_product_tree()
    root.print_tree()
    print(root.get_level())
    pass