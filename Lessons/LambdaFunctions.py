# Lambda Functions is a small anonymous function without a name

numDoubler= lambda num:num*2
print(numDoubler(4))

# we can pass function as an argument to another function
def mainFunction(secFunction,value):
    print(10+secFunction(value))

mainFunction(lambda num:num*num,6) # Here We Have Passed Lambda Function as an argument 


# MAP Function
# The map Function applies a function to each element in sequence & returns a new sequence containing transformed elements

myNumList=[1,2,3,4,5,6,7,8,9,10]
cuber=map(lambda nums:nums*nums*nums,myNumList)
print(tuple(cuber))


# Filter Function
# The filter function filters a sequence of element based on give predicate and returns a new sequence containing only the element that meet the predicate
filteredList=list(filter(lambda nums:nums>10,myNumList))
print(filteredList)

# Reduce Function
# Function takes two arguments and returns a single value
from functools import reduce
multiplayer= reduce(lambda el1,el2:el1*el2,myNumList)
print(multiplayer)