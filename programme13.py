s1=int(input())
if s1 > 1:
    for k in range(2,s1):
        if(s1%k==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
