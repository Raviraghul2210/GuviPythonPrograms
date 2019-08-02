r=input()
a=0
for i in r:
	if i.isnumeric():
		pass
	elif i.isalpha():
		pass
	elif i.isspace():
		pass
	else:
		a+=1
print(a)
