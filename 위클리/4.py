import copy
import sys
sys.setrecursionlimit(10**8)
def dp(b, i, c, st):
    if i==len(b): 
        st.add(tuple(c))
    elif i==0 or i-b[i][1]<0 or b[i][0]!=b[i-b[i][1]][0]: 
        dp(b,i+1,copy.deepcopy(c),st)
    else:
        tmpb = b[:]
        tmpb[i] = [b[i][0]*2,b[i-1][1]+b[i][1]]
        tmpc = c[:]
        tmpc.append(i)
        dp(tmpb,i,tmpc,st)
        dp(b,i+1,copy.deepcopy(c),st)
            
def solution(a, s):
    i = 0
    answer = []
    for j in s:
        tmp = a[i:i+j]
        for idx, t in enumerate(tmp):
            tmp[idx] = [t,1]  #
        st = set()
        tmp2 = dp(tmp,0,[],st)
        answer.append(len(st))
        i+=j
        

    return answer

print(solution([1,1,1,1,1,1,2,5,8,2,1,1,4,8,8,8,12,6,6],[4,3,1,5,6]))