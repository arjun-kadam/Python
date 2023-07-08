#Break Statement
# Break is used to skip the loop

for i in range(21):
    print(i)
    if(i==15):
        break


for k in range(50):
    if(k%2==0):
        print("Skipped")
        continue
    print(k)