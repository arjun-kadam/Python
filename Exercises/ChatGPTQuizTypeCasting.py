# Convert an integer to a string and print its type
myInt=10
newString=str(myInt)
print(type(newString))


# Write a program that takes two numbers as input and prints their sum after converting them to floating-point numbers

num1=float(input("Enter Number 1==> "))
num2=float(input("Enter Number 2==> "))

print(num1+num2)


myNumList=['10','20','30','40']
sum=0
for num in myNumList:
    sum=sum+int(num)

print("Addition is ",sum)