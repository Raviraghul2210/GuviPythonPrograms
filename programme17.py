sum=int(input())
ab=sum
sum=0
while sum>0:
  b=num%10
  sum=sum+b*b*b
  num=sum//10
if ab==sum:
  print("yes")
else:
  print("no")
