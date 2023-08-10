print("Welcome To Kaun Banega Karodpati!!!!")
userName=input("Please Enter Your Name: ")
print(f"Hello {userName} !!! ")

def showQuestions():
    qList=["Who is Prime Minister Of India?","Who Made 100 Centuries in Cricket?","What is 0!=?"]
    for questions in qList:
        print(questions,"\n")

def readyToGo():
    userReady=input("Do You want to Start??(Y/N): ")
    if(userReady=="Y"or userReady=="y"):
         print("Here is your Questions ==>\n")
         showQuestions()
    elif(userReady=="N"or userReady=="n"):
         print("Then Why You are Here?? Go Home(Nikal)")
    else:
        print("Wrong Choice!! Please Enter Y or N")
        readyToGo()
readyToGo()
