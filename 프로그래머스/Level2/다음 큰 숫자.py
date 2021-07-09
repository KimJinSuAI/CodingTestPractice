from collections import Counter
def solution(n):
    m = n+1
    while Counter(bin(n))['1']!=Counter(bin(m))['1']:
        m +=1
    return m
print(solution(78))