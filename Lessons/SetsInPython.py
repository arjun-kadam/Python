# Well Defined Objects
# Unordered Collection Of Data
# Set Do Not Contain Duplicate Values
# Sets Are Immutable

mySet={12,25,15,11,10}
print(mySet)

myEmpSet={} #This is Empty Dictionary
myRealEmpSet=set() # This is Empty Set
print(type(myEmpSet))
print(type(myRealEmpSet))


# Operations On Sets
mySet1={10,13,9,6,12,19,45,22,43}
mySet2={34,18,40,44,13,11,9,5,19}

#Union 
print("Union Set: ",mySet1.union(mySet2)) #print values of both set excepting Duplicate values

# Intersection
print("Intersection Set: ",mySet1.intersection(mySet2)) # Print Common Values

# Symmetric Difference
print("Symmetric Difference: ",mySet1.symmetric_difference(mySet2)) # not similar in both sets

# Difference 
print("Difference: ",mySet1.difference(mySet2))


# Methods In Sets

# isdisjoint()
print("Is Disjoint: ",mySet1.isdisjoint(mySet2))

# issuperset()
print("Is Super Set: ",mySet1.issuperset(mySet2))

# issubset()
print("Is Sub Set: ",mySet1.issubset(mySet2))

# Add Single item to set
mySet1.add(12)
print("Added Single Element: ",mySet1)

# Add More Then One item
newSet={77,66}
mySet2.update(newSet)
print("Added Multiple Element: ",mySet2)

# Remove From Set with remove()
mySet2.remove(44)
print("Removed Single Element: ",mySet2) #If Item Not found It will throw error

# Remove From Set with discard()
mySet2.discard(44)
print("Removed Single Element: ",mySet2) #If Item Not found It will not throw error


# Del keyword to delete set
delSet={"hey", "Hello","Namaste"}
del delSet
# print(delSet) # Throws an Error

#Use To delete all item in sets
clearSet={11,22,33,44,55,66}
clearSet.clear()
print("Cleared Set: ",clearSet)

#Check if Element is present or Not
if 44 in clearSet:
    print("Yes")
else:               #This will print No because we cleared Set in previous method(Line 68)
    print("No")