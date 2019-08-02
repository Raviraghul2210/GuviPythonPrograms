r=int(input())
y = list(map(int, input().split()))
y.sort()
n=len(x)
if(n%2!=0):
    z=(n)//2
    print(y[z])
else:
    ans=y[n//2]+y[(n-1)//2]
    j=ans/2
    print(j)
