# Special Method in a class used to create and initialize an object of a class
# Constructor is invoked automatically when an object is created
# Types: 1) Default 2)Parameterized

class NameDisplayer:
    def __init__(self): # Default Constructor 
        print("My Name is Arjun From Default Constructor")

class Adder: # Parameterized Constructor
    def __init__(self,a,b):
        print(f"Addition of {a} and {b} is: ", a+b)


obj1=NameDisplayer()
obj2=Adder(5,7)


