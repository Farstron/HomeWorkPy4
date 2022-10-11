import random
import fudata
k = int(input())
k2 = int(input())
res = ' '
res2 = ' '
res = fudata.fill(k,res)
res2 = fudata.fill(k2,res2)
if k>k2:
    with open('from1.txt','w') as data:
        data.write(res)
    with open('from2.txt','w') as data:
        data.write(res2)
else: 
    with open('from2.txt','w') as data:
        data.write(res)
    with open('from1.txt','w') as data:
        data.write(res2)
