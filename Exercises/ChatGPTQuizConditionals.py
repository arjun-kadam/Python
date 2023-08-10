# Write a program to check if a given number is positive, negative, or zero
# uInput=int(input("Enter A Number ===> "))
uInput=2
if uInput>0:
    print("Number is Positive")
elif uInput==0:
    print("Number is Zero")
else:
    print("Number is Negative")

# Given the age of three people, write a program to find the oldest person

p1=100
p2=99
p3=88

if p1>p2 and p1>p3:
    print("P1 is Older")
elif p2>p1 and p2>p3:
    print("p2 is Older")
else:
    print("P3 is Older")



# Write a program that takes a year as input and determines if it is a leap year or not
yearInput=int(input("Enter a Year==> "))
if (yearInput % 4 == 0 and yearInput % 100 != 0) or (yearInput % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
