num=int(input())
ab=num
sum=0
while num>0:
  b=num%10
  sum=sum+b*b*b
  num=num//10
if ab==sum:
  print("yes")
else:
  print("no")
