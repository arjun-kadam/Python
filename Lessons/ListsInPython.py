# Lists Are Collection Of Data Items 
# Contain any type of data type

myList=[1,2,3,4,"Arjun",2.9,True]
print(myList)

#positive Indexing
print(myList[3])

#Negative Indexing
print(myList[-3])

# Check whether element is present or not
if 3 in myList:
    print("Yes")
else:
    print("No")


#List Slicing
print(myList[1:4])
print(myList[-3:-1])

#Jump index   
print(myList[0:7:2])

