a=input()

b=input()

if a==b:
	raise RuntimeError
else:
	print(1/(int(a)-int(b)))
