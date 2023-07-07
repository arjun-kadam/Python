# String are anything that are enclosed within double or single quotes 
# String are Immutable

str1="This is first string"
print(str1)

str2="This is 'Highlighted Text'"
print(str2)

para='''This is long paragraph
        line 1
        line 2
        line n ''' 
print(para)

#looping In String
print("Looping Strings")
str3="DevOps"
for chars in str3:
    print(chars)

#String Slicing
print("String Slicing ")
newString="Hey This is Arjun Kadam" 
print("Length of String is: ",len(newString))

str3="ArjunKadam"
print(str3[3])
print(str3[1:4])
print(str3[1:]) #Exp: print(1:len(str3))
print(str3[:4])
print(str3[-4:-1]) #Exp: print(len(str3)-4:len(str3)-1)

