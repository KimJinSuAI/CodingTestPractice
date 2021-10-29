def solution(size):
    answer = 0
    for i in range(size//3, size//2):
        if i%2:
            answer+= 3*(i//2)-28
        else:
            answer+= 3*(i//2)-29
    return answer

print(solution(60))