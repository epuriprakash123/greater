A,B,C=[int(i) for i in input().split()]
if(A>B):
	if(A>C):
		print(A)
	else :
		print(C)
elif(B>C):
	print(B)
else :
	print(C)
