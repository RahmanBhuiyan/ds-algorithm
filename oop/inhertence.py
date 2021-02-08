class Person:
  def __init__(self,data):
    self.data=data
    print("preant class",data)
  def child(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self,data):
    super().__init__(data)
    print("child cass ")
  def preand (self):
    print(self.lastname)
x = Student(12)
x = Student(14)
x = Student(15)
x = Student(14)
x.child("chiil","bro") 
x.printname()
x.preand()