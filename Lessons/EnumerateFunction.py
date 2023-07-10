# By Using Enumerate Function we can extract index of list

myMarkList=[10,12,34,56,98,90,13]

for index,mark in enumerate(myMarkList):
    print(mark)
    if(index==4):
        print("You Are Excellent")


myMarkList2=[10,12,34,56,98,90,13]

for index2,marks in enumerate(myMarkList2,start=1):
    print(marks)
    if(index2==4):
        print("You Are Excellent")