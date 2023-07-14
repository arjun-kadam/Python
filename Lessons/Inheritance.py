# One Class is derive from another class
# It Inherits all public and protected methods from parent class

class BaseClass:
    def baseDetails(self):
        print("I am a Base Class")

class DerivedClass(BaseClass):
    def derivedDetails(self):
        print("I am From Derived Class")

d1=DerivedClass() 
d1.derivedDetails() # Method of Derived Class
d1.baseDetails() # Method Of Base Base Class