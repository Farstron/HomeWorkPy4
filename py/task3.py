lis1=[1,2,3,4,5,6,7,8,1,5,3,8,7,7,9,10,3,5]
lis2=[]
for i in lis1:
	if not(i in lis2):
		lis2.append(i)
print(lis2)