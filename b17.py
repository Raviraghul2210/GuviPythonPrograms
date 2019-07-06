inputnum=int(input())
sum=0
n=inputnum
while n>0:
    dig=n%10
    sum+=dig**3
    n//=10
    if(inputnum==sum):
        print('yes')
    else:
        print('no')
