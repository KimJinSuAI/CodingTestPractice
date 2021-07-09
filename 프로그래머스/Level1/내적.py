from functools import reduce
def solution(a, b):
    return reduce(lambda x,y:x+y,list(i*j for i,j in zip(a,b)),0)

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))