
myList=[3,2,4,5,7,9,10,8,1,6,11,56,99]
print(myList)
#sorting The List in Ascending
myList.sort()
#sorting The List in descending
myList.sort(reverse=True)
print(myList)

#reverse the list
myList.reverse()
print(myList)

#Add new element at the end
myList.append(14)
print(myList)


#Print given index of given element
ind=myList.index(10)
print(ind)

#Occurrence of any element
occ=myList.count(10)
print(occ)

#copying List
myList2=[10,11,12,13]
copiedList=myList2.copy()
copiedList[0]=30
print(copiedList)

#list Inserting at given index 
#It does not change element but insert at that index
myList3=[21,33,44,55]
print(myList3)
myList3.insert(1,31)
print(myList3)

