# Methods that belong to class rather than instance of class
# Need to give @staticmethod before declaring method


class AdditionMath:
    def getValue(self,a,b):
        self.a=a
        self.b=b
        print(f"Value of a is {a}")
        print(f"Value of b is {b}")

    @staticmethod
    def AddNums(a,b):
        print(f"Addition is {a + b}")

m1=AdditionMath()
m1.getValue(10,20)
m1.AddNums(10,33)
AdditionMath.AddNums(10,2)