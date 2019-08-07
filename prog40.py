rr=int(input())
if rr!=0:
	print(1,end=' ')
	j1=1
	k1=0
	for i in range(1,rr):
		z1=k1+j1
		print(z1,end=' ')
		k1=j1
		j1=z1
else:
	print(0)
