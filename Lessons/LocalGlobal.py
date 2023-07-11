# Local Variables are accessible into only particular function
# Global Variable can be accessed from anywhere

#Global Variable
x=10
def myfunc():
    y=19 #Local Variable
    print(y)
myfunc()
#print(y)# This will throw error


#How to change global variable from function
gVar=40
def gVarChanger():
    global gVar
    gVar=50
gVarChanger()
print(gVar) # This Will Print Changed Value


