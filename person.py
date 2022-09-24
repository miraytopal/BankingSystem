class Person:

  def __init__(self,ID,name,surname):
    self.ID = ID
    self.name = name
    self.surname = surname
    self.__str__()

  def __str__(self):
    print(f'Welcome to Trust Bank App Mr.\Mrs.{self.name} {self.surname}')