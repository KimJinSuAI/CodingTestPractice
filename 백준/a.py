# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    El = 0
    Ol = 0
    for i in range(len(A)):
        if i%2: 
            Ol = max(Ol,A[i])
        else:
            El = max(El,A[i])
    return (Ol+El)
print(solution([5,3,10,6,11]))
