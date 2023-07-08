# f-Strings Are Used to manipulate the strings in python

#Before f-strings
intro="Hello My Name is {} and I am From {}"
name="Arjun"
country="India"
print(intro.format(name,country)) # Right 
print(intro.format(country,name)) #Wrong


#after f-Strings
Lang="Python"
channel="CWH"
myIntro=f"Hello Everyone, We Are Learning {Lang} from {channel}"
print(myIntro)

print(f"{3*12}") #data type is String

#printing as it is f-strings
myWords=f"Hey There I am {{name}}"
print(myWords)


