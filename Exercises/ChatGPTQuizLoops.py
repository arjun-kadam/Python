# Write a loop to print numbers from 1 to 5

for i in range(6):
    print(i)



#  Write a program to calculate the factorial of a given number using a while loop

# uInput=int(input("Enter Number For Factorial==> "))
# factorial=1
# while uInput>=1:
#     factorial*=uInput
#     uInput-=1

# print(factorial)


# Given a list of numbers, write a program to find the largest number using a for loop
numList=[2,32,4,7,655,21,12,35,45,64,1,3,66,45]
largeNum=numList[0]
for num in numList:
    if num > largeNum:
        largeNum=num

print("Large Num is ==>", largeNum)