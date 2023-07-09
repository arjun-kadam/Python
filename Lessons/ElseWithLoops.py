#We Can Use Else Within The Loops

#This Will Execute else after completing Loop
for i in  range(10):
    print(i)
else:
    print("I am out of Loop")

#Else is not executed if we use Break in between loop
for k in range(10):
    print(k)
    if(k==6):
        break
else:
    ("I am out of Loop")