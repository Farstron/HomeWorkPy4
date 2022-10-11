import random
k = input('Введите число:')
res = ' '
while int(k)!=0:
	a = str(random.randrange(0,100))
	res =res+a+'*'+'x^'+str(k)+" + "
	k=int(k)-1
a = str(random.randrange(0,100))
with open('from1.txt','w') as data:
	data.write(res+a+' = 0')