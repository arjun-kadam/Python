# Ordered Collection Of Element In Python
# Items are in key value pair

myInfo={
    "Name":"Arjun",
    "DOB":"29-01-2001",
    "CGPA":8.32,
    "isVoter":True,
    "isMarried":False
}

print(myInfo)

print(myInfo["CGPA"]) #print particular item if not found throws error
print(myInfo.get("DOB")) #print particular item if not found does not throws error
print(myInfo.keys()) #display all keys
print(myInfo.values()) # display all Values
print(myInfo.items()) # display all Key-Value Pairs


## Dictionary Methods

#Update Information
myInfo.update({"Location":"Pune"})
print(myInfo)

           #OR#
newInfo={
    "Lang":"HTML,CSS,Python",
    "isValid":True
}

myInfo.update(newInfo)
print(myInfo)

# Remove all elements
newInfo.clear()
print(newInfo)

#Remove Particular item

myInfo.pop("isMarried")
print(myInfo)

#Remove Last Item From Dictionary
myInfo.popitem()
print(myInfo)

#Delete Dictionary
myNewDict={
    10:"10%",
    20:"20%"
}
del myNewDict[10] #delete particular key pair
print(myNewDict)
del myNewDict #delete all values
