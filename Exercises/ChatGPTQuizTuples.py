#  Create a tuple containing three different data types and print the tuple
myTuple=(10,"Tuple",True)
print(myTuple)
# print(type(myTuple))

# Swap the values of two tuples and print the updated tuples
myTup1=(10,20,30)
new2=myTup1
myTup2=(50,60,70)

print("Before Swap Tuple 1==> ",myTup1)
print("Before Swap Tuple 2==> ",myTup2)
myTup1=tuple(list(myTup2))
myTup2=tuple(list(new2))

print("After Swap Tuple 1==> ",myTup1)
print("After Swap Tuple 2==> ",myTup2)


# Write a function that takes a list of tuples as input and returns a new list containing the second element of each tuple.

def secondIndexList(input_list):
    output_list=[]
    for inList in input_list:
        output_list.append(inList[1])
    
    return output_list

input_list=[(1,"a"),(2,"b"),(3,4)]
print(secondIndexList(input_list))
