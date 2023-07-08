
#block of code that perform specific tasks
import cmath
def areaOfCircle(rad):
    print(cmath.pi*(rad)**2) #function definition

areaOfCircle(12) #function call


def areaOfSquare(area=4):
    print("Area of Square is: ", area**2) #function with default argument

areaOfSquare() #Invokes default argument
areaOfSquare(7) #Invokes given argument


#Sequence of arguments
#Required arguments
def areaOfRect(length,breadth):
    print("Area Of Rectangle is: ",length*breadth)

areaOfRect(4,1) 
areaOfRect(breadth=12,length=10)

# Variable length arguments 

def avgCalc(*nums):
    finalAvg=0
    for num in nums:
        finalAvg=finalAvg+num
    print("Average Of Given Numbers: ",finalAvg/len(nums))

avgCalc(10,20)


