class MyFirstClass: # Class
    def myDetails(self,name): #Class Methods 
        print(f"I am {name}")

obj1=MyFirstClass() #Object
obj1.myDetails("Arjun")

# Why We Use self argument 
# We have to it because that method takes object as an argument on which method is running

