import itertools
from functools import reduce
import math
def solution(numbers):
    answer = 0
    memo = {}
    for i in range(1,len(numbers)+1):   #1개뽑고 조합
        per = list(map(lambda x:reduce(lambda y,z : y+z,x) , set(itertools.permutations(numbers,i))))
        for j in per:                   #각조합에 대해서
            if memo.get(j)==1 or memo.get(j)==-1:
                continue
            if len(str(int(j)))!=i:
                continue
            q=int(math.sqrt(int(j)))
            for k in range(2,q+1): #소수인지 검사
                if int(j)%k==0:
                    memo[j]=-1
                    break
            if memo.get(j)!=-1 and int(j)>1:
                answer+=1
                memo[j]=1
    return answer