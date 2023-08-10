
def checkStringPalindrome(user_in):
    cleanedString=''.join(char.lower() for char in user_in if char.isalnum())
    temString=cleanedString[::-1]
    if len(cleanedString)==1:
        print("Equal")
    elif cleanedString==temString:
        print("Equal")
    else:
        print("not equal")

uInput=input("Enter Sentence Or Word \n===> ")
checkStringPalindrome(uInput)