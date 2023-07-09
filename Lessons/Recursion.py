#Function Call Itself
#Factorial Program

def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*factorial(num-1) # Recursion is Used 

print(factorial(5))
