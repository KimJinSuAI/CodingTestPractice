import math
def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))

# print(solution(3,5))
# print(solution(1,1))
print(solution(98,2))
print(solution(2,98))