# Public  
# Can Be Accessed from anywhere
# Default Access Modifier 

# Private 
# Only Accessible within class

# Protected 
# It accessible with class and subclass


class Fruits:
    def __init__(self):
        self._privateAtr="I am Private"
        self.__mangledAtr="I am Mangled"

f1=Fruits()
print(f1._privateAtr)
print(f1._Fruits__mangledAtr)
print(f1.__mangledAtr)
