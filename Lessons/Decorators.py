# Python decorators are powerful and versatile tool that allows you to modify the behavior of functions and methods
# It takes another function as an arguments

def Welcomer(fx):

    def newFun(*b,**a):
     print(" Welcome to My Program")
     fx(*b,**a)
    return newFun

@Welcomer
def additionFunction(a,b):
    print("The Addition is:", a+b)

additionFunction(2,3)