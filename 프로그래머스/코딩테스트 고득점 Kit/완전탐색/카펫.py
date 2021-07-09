import math
def solution(brown, yellow):
    h = int((brown/2+2-math.sqrt(math.pow(brown/2+2,2)-4*brown-4*yellow))/2)
    w = int(brown/2+2-h)
    answer = [w,h]
    return answer
print(solution(24,24))