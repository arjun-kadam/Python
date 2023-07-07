#If Else
age=int(input("Enter Your Age: "))
if(age>=18):
    print("Congrats!!! You Can Vote")
    if(age>100):
     print("But You Might Be Dead")
else:
    print("Oh No!!! You Cannot Vote\n")
    print("But You Can Vote After",18-age,"Year")

#elif

uInput=int(input("Enter Any Number: "))
if(uInput<0):
    print("The Number is Negative")
elif(uInput==0):
    print("The Number is Zero")
else:
    print("Number is Positive")

