import fudata as fun

data = open('from1.txt','r')
res1=data.readline()
data.close()

data = open('from2.txt','r')
res2=data.readline()
data.close()

sum = ' '
dic_sum = {}
fun.creat_dic(res1,dic_sum)
fun.creat_dic(res2,dic_sum)

with open('out.txt','w') as data:
	data.write(fun.sum(dic_sum))