# Printing Fibonacci Series

def fibo(length):
    num1=0
    num2=1
    count=0
    if(length<=0):
        print("Enter Positive Number: ")
    elif length ==1:
        print("Fibo for ",length, "is ",1)
    else:
        while count<length:
            print(num1)
            nextNum=num1+num2
            num1=num2
            num2=nextNum
            count+=1

lengthInput=int(input("Enter Length Of Fib Series: "))
fibo(lengthInput)

