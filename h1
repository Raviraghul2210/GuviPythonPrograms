from collections import Counter
num1=int(input())
num2=list(map(int,input().split()))
num3=Counter(num2)
list=[]
for x in num3.items():
  if(x[1] != 1):
   print(x[0],end ='')
for y in num3.items():
  list.append(y[1])
if(max(list) == 1):
  print("unique")
