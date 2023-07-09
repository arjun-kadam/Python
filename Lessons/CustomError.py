# We can produce custom error in python

a=int(input("Enter any value between 10 to 20: "))

if(a<10 or a>20):
    raise ValueError("You Don't Have eyes!!! Enter Number Between 10 to 20")
else:
    print("You are Good!!!")