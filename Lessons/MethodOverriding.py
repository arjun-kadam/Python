# Allows you to redefine a method in derived class

class Animal:
    def __init__(self,name,types):
        self.name=name
        self.types=types
    def showAnimal(self):
        print(f"Type Of Animal is {self.types} and name is {self.name}")

class FourLegAnimal(Animal):
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def showAnimal(self):
        print(f"The Animal is {self.name} and is of {self.species} Species")

cow=Animal("Cow","Canadian")
cow.showAnimal()