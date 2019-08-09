from itertools import combinations
ra,p=list(input().split())
k=[]
p=int(p)
length=combinations(ra,len(ra)-p)
for i in length:
  k.append("".join(i))
print(min(k))
