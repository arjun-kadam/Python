f=open('Exercises/input.txt','r')
count=0

while True:
    data=f.read(1)
    count+=1
    if not data:
        break
print(count)