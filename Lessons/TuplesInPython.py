#Collection Of Data Items ]
# Tuples Are Immutable (Not Changeable)

myTuple=(1,2,4,5,6,7,3,4,5,6,2,3,42,2,3,3,3,3,3,3)
print(myTuple)

#It Has Same Indexing operation like Lists

#indirect way to change Tuple

originalTuple=(10,20,30,40,50)
tempList=list(originalTuple) #convert tuple to List
tempList.append(60) #modify List

originalTuple=tuple(tempList) #Convert List into Tuple
print(tempList)


#concat two Tuples
tup1=("Arjun ")
tup2=("Kadam")
tup3=tup1+tup2
print(tup3)



#Tuple Methods

#Gives the count of given value
print(myTuple.count(3))

#index of given value
print(myTuple.index(5))