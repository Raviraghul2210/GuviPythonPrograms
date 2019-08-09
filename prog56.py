r=(input())
a=len(r)
count=0
sum1=0
for x in range (a):
  if (r[x].isdigit()):
    count=count+1
  elif(r[x].isalpha()):
    sum1=sum1+1
if(count!=0 and sum1!=0):    
  print('Yes')
else:
  print('No') 
