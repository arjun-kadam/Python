# Class Variables defined outside to the class and shared among all methods belong to class
# Instance Variables defined atr instance level and are unique to each instance of class

class StudentData:
    clgName="Parikrama" # Class Variable
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.fees=30 # Instance Variable

    def ShowStudDetails(self):
        print(f" ID No: {self.id} is {self.name} from {self.clgName} and Fees are {self.fees}K")

std1=StudentData("Arjun","101")
std1.ShowStudDetails()

std2=StudentData("Vaibhav","123")
std2.clgName="PICT" # Not Necessary to change
std2.fees=80
std2.ShowStudDetails()
