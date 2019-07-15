A,E=map(int,input().split())
for u in range(A+1,E):
    for v in range(2,u):
       if(u%v==0):
           break
    else:   
        print(u,end=" ")
