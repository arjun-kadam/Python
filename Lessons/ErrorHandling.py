# Exception is the process of responding to unwanted events when program runs 
# Used to deal with Errors

num1=int(input("Enter 1st Number :"))
num2=int(input("Enter 2st Number :"))

try:
    print("Division Of Numbers is",num1/num2)
except:
    print("Enter Non zero at 2nd Number!!!")

# We Can USe Multiple Except Statements
