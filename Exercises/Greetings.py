from time import strftime
getTime=int(strftime("%H"))

if(getTime>=5 and getTime <=12):
    print("Good Morning")
elif(getTime>=12 and getTime<19):
    print("Good Afternoon")
elif((getTime>=20 and getTime<=23) or (getTime>=00 and getTime<=4)):
    print("Good Night")
else:
    print("Time is Not Correct!!!")