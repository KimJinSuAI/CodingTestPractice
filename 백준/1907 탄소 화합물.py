from collections import defaultdict
from copy import deepcopy
import sys
import re
input = sys.stdin.readline

exp = input()[:-1].replace('+','=').split('=')
num = [dict() for _ in range(3)]
ans = []
for i in range(len(exp)):
    ch = ''
    for j in range(len(exp[i])):
        if re.findall('[A-Z]',exp[i][j]):
            if len(ch)==2:
                num[i][ch[0]] = num[i].get(ch[0],0)+int(ch[1])
            elif len(ch)==1:
                num[i][ch[0]] = num[i].get(ch[0],0)+1
            ch = exp[i][j]
        else:
            ch+=exp[i][j]
    
    if len(ch)==2:
        num[i][ch[0]] = num[i].get(ch[0],0)+int(ch[1])
    elif len(ch)==1:
        num[i][ch[0]] = num[i].get(ch[0],0)+1



for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            flag = True
            tmp = deepcopy(num)
            for key in num[2].keys():
                tmp[2][key] = k*tmp[2][key] - i*tmp[0].get(key,0) - j*tmp[1].get(key,0)
                if tmp[2][key] !=0:
                    flag = False
                    break
            if flag:
                ans.append((i,j,k))
        
print(*sorted(ans)[0])