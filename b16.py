x,y=map(int,input().split())
for u in range(x+1,y):
    for v in range(2,u):
       if(u%v==0):
           break
    else:   
        print(u,end=" ")
