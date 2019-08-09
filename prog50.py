range = int(input())
a = 0
for i in range(0,r+1):
    if pow(2,i)==r:
        a+=1
if(a>0):
    print("yes")
else:
    print("no")
