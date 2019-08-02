v=int(input())
ls=list(map(int,input().split()[:v]))
for i in range(v):
  print(ls[i],i)
