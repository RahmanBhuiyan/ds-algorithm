class Father:
  def __init__(self):
    super().__init__()  
    print("preant class")
  def printname(self):
    print("walid ")
class Mother:
  def __init__(self):
    super().__init__()
    print("child class ")
class son(Father,mother):printname
  def __init__(self):
    super().__init__()
    print("son class")
    

x = son()
x.printname()

