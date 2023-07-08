# Doc Strings Are written immediately after function declaration and before function definition

def squares(nums):

    '''This is Paragraph
    Line 1 
    Line 2
    Line 3 '''
    print("Square is: ",nums**2)

squares(12)

print(squares.__doc__) #this will print Doc-Strings