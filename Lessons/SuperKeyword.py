# super() keyword in python is used to refer to the parent class

class ClgTeacher:
    bonus=1000
    def __init__(self,name,sub,salary):
        self.name=name
        self.sub=sub
        self.salary=salary
    
    def viewTeacher(self):
        print(f"The Teacher Name {self.name} is teaching {self.sub} Subject")
    
    def salaryCalc(self):
        return self.salary + self.bonus
    
class PlacementTeacher(ClgTeacher):
    def __init__(self,name,sub,salary,payment):
        self.name=name
        self.sub=sub
        self.salary=salary
        self.payment=payment
        super().__init__(name,sub,salary)

    def viewTeacher(self):
        print(f"The Teacher Name {self.name} is teaching {self.sub} Subject")

    def totalPayment(self):
        return self.payment + super().salaryCalc()


teacher1=PlacementTeacher("Arjun","IoT",10000,5000)
teacher1.viewTeacher()
print("Total Payment Received ",teacher1.totalPayment())

