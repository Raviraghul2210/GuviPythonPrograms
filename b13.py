n1=int(input())
if n1 > 1:
    for k in range(2,n1):
        if(n1%k==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
