import random
def fill(k,res):
    a = str(random.randrange(0,100))
    if k!=0:
        return fill(k-1,res+a+'*'+'x^'+str(k)+" + ")
    return res+a

def creat_dic(res, dic_sum={}):
    op = ['*','-','^','x',' ','+']
    i=0
    temp = 0
    while i<len(res):
        if res[i-1]=='^':
            dic_sum.update({int(res[i]):temp})
            temp = 0
            i+=1
        if not(res[i] in op):
            if temp<0:
                temp = temp*10 - int(res[i])
            if res[i-1]=='-':
                temp-=int(res[i])
            else: temp = temp * 10 + int(res[i])
        i+=1
    dic_sum.update({0:temp})
    return dic_sum

def sum(dic_sum,sum = ' '):
    i = 0
    while i < len(dic_sum)-1:
        sum=sum+str(dic_sum.get(len(dic_sum)-1-i))+'*x^'+str(len(dic_sum)-1-i)+' + '
        i+=1
    return sum+str(dic_sum.get(len(dic_sum)-1-i))