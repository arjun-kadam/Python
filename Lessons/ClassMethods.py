# Type of method that is bound to the class and not the instance of class

class StudentData:
    branch="CSE"
    def studName(self):
        print(f"Name is {self.name} and Branch is {self.branch}")
    
    @classmethod
    def changeBranch(cls,newBranch):
        cls.branch=newBranch

std1=StudentData()
std1.name="Arjun"
std1.studName()

std2=StudentData()
std2.name="Prashant"
std2.changeBranch("AI")
std2.studName()

print(StudentData.branch) # Branch Changed For Other Instances too

std3=StudentData()
std3.name="Vaibhav"
std3.studName()