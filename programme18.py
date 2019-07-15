B,S=map(int,input().split())
for m in range(B+1,S):
    sum=0
    num=m
    while num>0:
        dig=num%10
        sum+=dig**3
        num//=10
        if(m==sum):
            print(m,end=" ")
