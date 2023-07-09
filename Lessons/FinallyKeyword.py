# Finally is used to run block of code after try catch block
# It used in functions

num1=int(input("Enter 1st Number :"))
num2=int(input("Enter 2st Number :"))

try:
    print("Division Of Numbers is",num1/num2)
except:
    print("Enter Non zero at 2nd Number!!!")
finally:
    print("I am Always run")

# Finally will run after running or using return function 
def lessValue(a,b):
    try:
        print(f"{a}/{b} :",a/b)
        return 1
    except:
        print("Dont put Zero")
        return 0
    finally:
        print("I am Devil I am Always Run")

num1=int(input("Enter a: "))
num2=int(input("Enter b: "))
x=lessValue(num1,num2)
print("Returned Value: ",x)