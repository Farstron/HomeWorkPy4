N = int(input())
proslis = []
i = 2
c=1
while i<=N:
	if N % i == 0:
		c=0
		for j in proslis:
			if i%j==0:
				c+=1
	if c == 0:
		proslis.append(i)
		c=1
	i+=1
proslis.reverse()
proslis.append(1)
proslis.reverse()
print(proslis)