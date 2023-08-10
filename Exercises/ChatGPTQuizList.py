# Create a list containing the names of three fruits and print the list.

fruitList=['mango','banana','orange']
print(fruitList)
# print(type(fruitList))



# Append a new fruit to the existing list and print the updated list
fruitList.append('Apple')
print(fruitList)


# Given a list of numbers, write a program to find the sum of all the even numbers in the list
numList=[2,8,6,5,3,9,7,15,14,4,19,11,16]
sum=0
for num in numList:
    if num%2==0:
        sum+=num

print(sum)