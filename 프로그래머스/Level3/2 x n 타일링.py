def solution(n):
    one, two, three = 1,2,3
    for i in range(n-3):
        one, two, three = two, three, two+three
    return three%1000000007

print(solution(4), 5)
print(solution(5), 8)
print(solution(6), 13)
print(solution(7), 21)
print(solution(8), 34)
print(solution(60000))
# print(solution(6000))