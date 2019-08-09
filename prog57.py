r,a=map(int,input().split())
num=list(map(int,input().split()))[:r]
count=0
for x in range (0,r):
  if a==num[x]:
    count+=1
print(count)
