def solution(s):
    return ''.join(sorted(s, reverse= True, key=lambda x: ord(x)))

print(solution("Zbcdefg"))